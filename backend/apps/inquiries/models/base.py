from django.db import models

from apps.core.models import Country, SoftDeletionWithUserModel, UserTrackingModel
from config import settings


class InquiryBaseModel(UserTrackingModel, SoftDeletionWithUserModel):
    class StatusChoices(models.TextChoices):
        PROCESSING = 'processing', 'Processing'
        PROCESSED = 'processed', 'Processed'
        ERROR = 'error', 'Error'
        OTHER = 'other', 'Other'

    class ImportanceChoices(models.TextChoices):
        UNKNOWN = 'unknown', 'Unknown'
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    inquirer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name='%(class)s_inquirer', verbose_name='Inquirer',
                                 help_text='Inquirer of the inquiry')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the inquirer')

    email = models.EmailField(max_length=255, verbose_name='Email', help_text='Email of the inquirer')

    organization = models.CharField(max_length=255, blank=True, null=True, verbose_name='Organization',
                                    help_text='Organization of the inquirer')

    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='Position',
                                help_text='Position of the person making the inquiry')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='%(class)s_inquiries', verbose_name='Country',
                                help_text='Country of the person making the inquiry')

    content = models.TextField(max_length=6000, verbose_name='Content',
                               help_text='Message of the person making the inquiry')

    notes = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Notes',
                             help_text='Notes of the inquiry')

    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PROCESSING,
                              verbose_name='Status', help_text='Status of the inquiry')

    importance = models.CharField(max_length=20, choices=ImportanceChoices.choices, default=ImportanceChoices.UNKNOWN,
                                  verbose_name='Importance', help_text='Importance of the inquiry')

    is_inquirer_emailed = models.BooleanField(default=False, verbose_name='Is inquirer emailed',
                                              help_text='Is the inquirer emailed')

    is_respondent_emailed = models.BooleanField(default=False, verbose_name='Is respondent emailed',
                                                help_text='Is the respondent emailed')

    custom_data = models.JSONField(blank=True, null=True, verbose_name='Data', help_text='Custom data of the inquiry')

    class Meta:
        abstract = True

    @property
    def is_processed(self):
        if self.is_inquirer_emailed is True and self.is_respondent_emailed is True:
            return True
        return False
