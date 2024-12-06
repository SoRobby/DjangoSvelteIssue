from apps.core.custom_fields import KeyField
from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from django.core.validators import RegexValidator
from django.db import models, transaction

'''
Future options to evaluate and potentially change:
1. OneToOne relationship with model validation (currently what is implemented)
2. Use Generic Foreign Key to link the property to the property type
3. Use polymorphic model-relationship to link the property to the property type

'''


class PropertyLibrary(UserTrackingModel, SoftDeletionWithUserModel):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the property library')

    slug = models.SlugField(max_length=255, verbose_name='Slug', help_text='Unique slug of the property library')

    key = KeyField()

    is_builtin = models.BooleanField(default=False, verbose_name='Is built-in',
                                     help_text='Whether the property library is built-in or not')

    status = models.CharField(max_length=20, choices=StatusChoices.choices,
                              default=StatusChoices.PUBLISHED, verbose_name='Status',
                              help_text='Status of the node')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the property library')

    admin_notes = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        verbose_name = 'Property library'
        verbose_name_plural = 'Property libraries'

    def __str__(self):
        return f'{self.name} (id={self.pk})'

    def save(self, *args, **kwargs):
        # Check if is_builtin has changed
        is_builtin_changed = False
        if self.pk:
            old_instance = PropertyLibrary.objects.get(pk=self.pk)
            is_builtin_changed = old_instance.is_builtin != self.is_builtin

        # Use a transaction to ensure database consistency, change is only applied to database if all operations
        # succeed
        with transaction.atomic():
            super().save(*args, **kwargs)

            # If is_builtin has changed or this is a new instance, update related Properties
            if is_builtin_changed or not self.pk:
                self.properties.update(is_builtin=self.is_builtin)
