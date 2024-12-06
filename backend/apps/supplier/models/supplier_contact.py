from django.db import models

from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from config import settings
from .supplier import Supplier


class SupplierContact(UserTrackingModel, SoftDeletionWithUserModel):
    class ContactTypeChoices(models.TextChoices):
        GENERAL = 'general', 'General'
        SALES = 'sales', 'Sales'
        SUPPORT = 'support', 'Support'
        MEDIA = 'media', 'Media'
        CAREERS = 'careers', 'Careers'

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='contacts', verbose_name='Supplier',
                                 help_text='Supplier of the contact')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supplier_contacts',
                             blank=True, null=True, verbose_name='User', help_text='User of the contact')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the contact')

    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='Position',
                                help_text='Position of the contact')

    email = models.EmailField(max_length=255, unique=True, verbose_name='Email', help_text='Email of the contact')

    phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='Phone',
                             help_text='Phone number of the contact')

    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the contact')

    show_email = models.BooleanField(default=True, verbose_name='Show email',
                                     help_text='Whether to show the email address on the website')

    show_phone = models.BooleanField(default=True, verbose_name='Show phone',
                                     help_text='Whether to show the phone number on the website')

    receive_inquiries = models.BooleanField(default=True, verbose_name='Receive inquiries',
                                            help_text='Whether to receive inquiries from the website')

    class Meta:
        ordering = ['name']
        verbose_name = 'Supplier contact'
        verbose_name_plural = 'Supplier contacts'

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
