from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    Abstract base model providing core fields and functionality to derived models.

    Fields:
    - uuid: A unique identifier for each record, not editable.
    - date_created: A timestamp indicating when the record was created.
    - date_modified: A timestamp indicating the last time the record was modified.
    """

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name='UUID',
                            help_text='Unique identifier for the item')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created',
                                        help_text='Server date and time when the item was created modified')

    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified',
                                         help_text='Server date and time when the item was last modified')

    class Meta:
        abstract = True


class UserTrackingModel(BaseModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name='%(app_label)s_%(class)s_created_by', verbose_name='Created by',
                                   help_text='User who created the item')

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name='%(app_label)s_%(class)s_modified_by', verbose_name='Modified by',
                                    help_text='User who last modified the item')

    class Meta:
        abstract = True


class SoftDeletionModel(models.Model):
    date_deleted = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                        verbose_name='Date deleted',
                                        help_text='Server date and time when the item was deleted')

    is_deleted = models.BooleanField(default=False, verbose_name='Is deleted',
                                     help_text='Whether the item has been deleted or not')

    class Meta:
        abstract = True

    def soft_delete(self):
        if not self.is_deleted:
            self.is_deleted = True
            self.date_deleted = timezone.now()
            self.save(update_fields=['is_deleted', 'date_deleted'])


class SoftDeletionWithUserModel(SoftDeletionModel):
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='%(app_label)s_%(class)s_deleted_by', verbose_name='Deleted by',
                                   help_text='User who deleted the item')

    class Meta:
        abstract = True


class AddressModel(models.Model):
    """
    Abstract model that represents an address.

    Fields: address1, address2, city, postal_code, country, subnational_region
    """
    address1 = models.CharField(max_length=255, verbose_name='Address 1', help_text='Address line 1')

    address2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Address 2',
                                help_text='Address line 2')

    city = models.CharField(max_length=255, verbose_name='City', help_text='City of the address')

    postal_code = models.CharField(max_length=16, verbose_name='Postal code', help_text='Postal code of the address')

    country = models.ForeignKey('core.Country', blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='%(app_label)s_%(class)s_country',
                                verbose_name='Country', help_text='Country of the address')

    subnational_region = models.CharField(max_length=255, blank=True, null=True, verbose_name='Subnational region',
                                          help_text='State, province, or region')

    class Meta:
        abstract = True


class BaseFileModel(models.Model):
    """
    Abstract model that represents a file, with a name and description.

    The user will still need to add a ForeignKey to the file model to link it to another model.
    """

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the file')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description', help_text='Description of the file')

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def latest_version(self):
        return self.versions.order_by('-version').first()
    

class BaseFileVersionModel(models.Model):
    version = models.PositiveIntegerField(verbose_name='Version', blank=True, help_text='Version of the file')

    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description', help_text='Description of the file')

    checksum = models.CharField(max_length=64, editable=False, help_text='SHA-256 checksum of the file')

    class Meta:
        abstract = True
        ordering = ['-version']
        indexes = [
            models.Index(fields=['version']),
        ]


    def save(self, *args, **kwargs):
        """
        Note: If you create a save method in a model that is a subclass of an abstract model,
        the subclass save method will execute first, and then the abstract model save method will execute.
        """
        self.check_model_setup()

        related_field_name = self.file_field
        related_instance = getattr(self, related_field_name)

        if not self.pk:
            last_version = self.__class__.objects.filter(**{related_field_name: related_instance}).order_by('-version').first()
            self.version = (last_version.version + 1) if last_version else 1

        if self.file:
            self.size = self.file.size
            self.checksum = self.calculate_checksum()

        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f'{getattr(self, self.file_field).name} - v{self.version}'

    @property
    def file_field(self):
        raise NotImplementedError("Subclasses must define the `file_field` property.")

    def check_model_setup(self):
        if not hasattr(self, 'file'):
            raise NotImplementedError("Subclasses must define a `file` field.")
        if not isinstance(self.file_field, str):
            raise NotImplementedError("Subclasses must define the `file_field` property correctly.")
    
    def calculate_checksum(self):
        import hashlib
        sha256 = hashlib.sha256()
        for chunk in self.file.chunks():
            sha256.update(chunk)
        return sha256.hexdigest()