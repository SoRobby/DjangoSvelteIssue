import os
from io import BytesIO

from apps.core.models import Country, SoftDeletionWithUserModel, UserTrackingModel
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from PIL import Image

from .supplier_tag import SupplierTag


# Model
class Supplier(UserTrackingModel, SoftDeletionWithUserModel):
    LOGO_IMAGE_ASPECT_RATIO = 1 / 1
    LOGO_IMAGE_SIZE = (300, 300)
    LOGO_IMAGE_THUMBNAIL_SIZE = (100, 100)

    def raw_logo_upload_path(self, filename):
        extension = os.path.splitext(filename)[1]
        return f'supplier/{self.uuid}/logo/raw{extension}'

    def processed_logo_path(self, filename):
        return f'supplier/{self.uuid}/logo/logo.webp'

    def processed_logo_thumbnail_path(self, filename):
        return f'supplier/{self.uuid}/logo/thumbnail.webp'

    class NumberOfEmployeesChoices(models.TextChoices):
        # Following LinkedIn's number of employees choices
        EMPLOYEES_0_1 = '0-1', '0-1 employees'
        EMPLOYEES_2_10 = '2-10', '2-10 employees'
        EMPLOYEES_11_50 = '11-50', '11-50 employees'
        EMPLOYEES_51_200 = '51-200', '51-200 employees'
        EMPLOYEES_201_500 = '201-500', '201-500 employees'
        EMPLOYEES_501_1000 = '501-1000', '501-1000 employees'
        EMPLOYEES_1001_5000 = '1001-5000', '1001-5000 employees'
        EMPLOYEES_5001_10000 = '5001-10000', '5001-10000 employees'
        EMPLOYEES_10001_PLUS = '10001+', '10001+ employees'

    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'Active'
        ACQUIRED = 'acquired', 'Acquired'
        INACTIVE = 'inactive', 'Inactive'

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the supplier')

    legal_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Legal name',
                                  help_text='Legal name of the supplier')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug',
                            help_text='The slug based on the supplier name')

    acronym = models.CharField(max_length=16, blank=True, null=True, verbose_name='Acronym',
                               help_text='Acronym of the supplier')

    website = models.URLField(max_length=255, blank=True, null=True, verbose_name='Website',
                              help_text='Website of the supplier')

    facebook_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Facebook link',
                                    help_text='Facebook link of the supplier')

    instagram_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Instagram link',
                                     help_text='Instagram link of the supplier')

    linkedin_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Linkedin link',
                                    help_text='LinkedIn link of the supplier')

    youtube_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='YouTube link',
                                   help_text='YouTube link of the supplier')

    x_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='X link',
                             help_text='X link of the supplier')

    tagline = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tagline',
                               help_text='Short tagline of the supplier')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the supplier')

    number_of_employees = models.CharField(max_length=16, choices=NumberOfEmployeesChoices.choices, blank=True,
                                           null=True, verbose_name='Number of employees',
                                           help_text='Number of employees that are employed by the supplier')

    year_founded = models.PositiveIntegerField(blank=True, null=True, verbose_name='Year founded',
                                               help_text='Year the supplier was founded')

    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Meta title',
                                  help_text='Meta tag title of the supplier')

    meta_description = models.TextField(max_length=160, blank=True, null=True, verbose_name='Meta description',
                                        help_text='Meta tag description of the supplier')

    meta_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name='Meta keywords',
                                     help_text='Meta tag keywords of the supplier')

    tags = models.ManyToManyField(SupplierTag, blank=True, verbose_name='Tags', help_text='Tags of the supplier')

    logo_raw = models.ImageField(upload_to=raw_logo_upload_path, blank=True, null=True, verbose_name='Logo raw',
                                 help_text='Raw logo image of the supplier')

    logo = models.ImageField(upload_to=processed_logo_path, blank=True, null=True, verbose_name='Logo',
                             help_text=f'Processed logo image in WEBP format.\
                                       <br>Required image size: {LOGO_IMAGE_SIZE[0]}x{LOGO_IMAGE_SIZE[1]}\
                                       <br>Required image aspect ratio: {LOGO_IMAGE_ASPECT_RATIO}\
                                       <br>The main logo should be uploaded to the "logo_raw" field and the model will\
                                       properly process the logo to generate the "logo" and "logo_thumbnail" image and\
                                       set the value for those fields.')

    logo_thumbnail = models.ImageField(upload_to=processed_logo_thumbnail_path, blank=True, null=True,
                                       verbose_name='Logo thumbnail',
                                       help_text=f'Processed logo thumbnail image in WEBP format.\
                                       <br>Required image size: {LOGO_IMAGE_THUMBNAIL_SIZE[0]}x{LOGO_IMAGE_THUMBNAIL_SIZE[1]}\
                                       <br>Required image aspect ratio: {LOGO_IMAGE_ASPECT_RATIO}\
                                       <br>The main logo should be uploaded to the "logo_raw" field and the model will\
                                       properly process the logo to generate the "logo" and "logo_thumbnail" image and\
                                       set the value for those fields.')
    
    is_premium = models.BooleanField(default=False, verbose_name='Is premium', help_text='Whether the supplier is premium or not')

    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.ACTIVE,
                              verbose_name='Status', help_text='Status of the supplier')

    acquired_by = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='acquired',
                                    verbose_name='Acquired by', help_text='Supplier that acquired this supplier')

    blocked_countries = models.ManyToManyField(Country, blank=True, verbose_name='Blocked countries',
                                               help_text='Countries where the supplier is blacklisted')

    is_blacklisted = models.BooleanField(default=False, verbose_name='Is blacklisted',
                                         help_text='Whether the supplier is blacklisted or not')

    is_hidden = models.BooleanField(default=False, verbose_name='Is hidden',
                                    help_text='Whether the supplier is hidden or not')

    admin_notes = models.TextField(max_length=4000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Admin notes for the supplier')

    class Meta:
        ordering = ['name']
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self) -> str:
        if self.acronym:
            return f'{self.name} ({self.acronym})'
        else:
            return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def process_and_save_logo(self):
        # Ref> https://chat.openai.com/share/02479099-4516-4217-ac11-5e4e1e1e7a57
        if not self.logo_raw:
            return

        image = Image.open(self.logo_raw)

        if image.mode in ("RGBA", "P", "LA"):
            image = image.convert('RGB')

        # Process the main logo image
        main_image = image.resize(self.LOGO_IMAGE_SIZE, Image.LANCZOS)
        main_output = BytesIO()
        main_image.save(main_output, format='WEBP')
        main_output.seek(0)
        self.logo.save(os.path.splitext(self.logo_raw.name)[0] + '.webp',
                       ContentFile(main_output.read()), save=False)

        # Process the thumbnail image
        thumbnail_image = image.resize(self.LOGO_IMAGE_THUMBNAIL_SIZE, Image.LANCZOS)
        thumbnail_output = BytesIO()
        thumbnail_image.save(thumbnail_output, format='WEBP')
        thumbnail_output.seek(0)
        self.logo_thumbnail.save(os.path.splitext(self.logo_raw.name)[0] + '_thumbnail.webp',
                                 ContentFile(thumbnail_output.read()), save=False)


# Signals
@receiver(pre_save, sender=Supplier)
def set_slug(sender, instance, *args, **kwargs):
    if not instance.pk or (instance.pk and Supplier.objects.get(pk=instance.pk).name != instance.name):
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Supplier)
def pre_save_supplier(sender, instance, **kwargs):
    if instance.pk:
        old_obj = Supplier.objects.get(pk=instance.pk)
        if old_obj.logo_raw != instance.logo_raw:

            # Logo has changed, delete old images
            if old_obj.logo_raw:
                old_obj.logo_raw.delete(save=False)
                if old_obj.logo:
                    old_obj.logo.delete(save=False)
                if old_obj.logo_thumbnail:
                    old_obj.logo_thumbnail.delete(save=False)
            # Process and save new images
            instance.process_and_save_logo()
    else:
        # For new instances, process and save logo
        instance.process_and_save_logo()


@receiver(post_delete, sender=Supplier)
def post_delete_supplier(sender, instance, **kwargs):
    if instance.logo_raw:
        instance.logo_raw.delete(False)
    if instance.logo:
        instance.logo.delete(False)
    if instance.logo_thumbnail:
        instance.logo_thumbnail.delete(False)
