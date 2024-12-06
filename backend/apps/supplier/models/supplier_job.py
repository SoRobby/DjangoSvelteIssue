from django.core.exceptions import ValidationError
from django.db import models

from apps.core.models import AddressModel, SoftDeletionWithUserModel, UserTrackingModel
from .supplier import Supplier
from .supplier_tag import SupplierTag


class SupplierJob(UserTrackingModel, SoftDeletionWithUserModel, AddressModel):
    class StatusChoices(models.TextChoices):
        ARCHIVED = 'archived', 'Archived'
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    class WorkplaceSettingChoices(models.TextChoices):
        REMOTE = 'remote', 'Remote'
        HYBRID = 'hybrid', 'Hybrid'
        ONSITE = 'onsite', 'Onsite'

    class EmploymentTypeChoices(models.TextChoices):
        FULL_TIME = 'full_time', 'Full-time'
        PART_TIME = 'part_time', 'Part-time'
        CONTRACT = 'contract', 'Contract'
        INTERNSHIP = 'internship', 'Internship'
        OTHER = 'other', 'Other'

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='jobs', verbose_name='Supplier',
                                 help_text='Supplier of the job')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the job')

    tags = models.ManyToManyField(SupplierTag, blank=True, verbose_name='Tags', help_text='Tags of the job')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the job')

    application_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Application link',
                                       help_text='Application link for the job')

    status = models.CharField(max_length=16, choices=StatusChoices.choices,
                              default=StatusChoices.PUBLISHED, verbose_name='Status',
                              help_text='Status of the job')

    posting_start_date = models.DateField(blank=True, null=True, verbose_name='Posting start date',
                                          help_text='Date when the job posting starts')

    posting_end_date = models.DateField(blank=True, null=True, verbose_name='Posting end date',
                                        help_text='Date when the job posting ends')

    workplace_setting = models.CharField(max_length=16, choices=WorkplaceSettingChoices.choices, blank=True, null=True,
                                         verbose_name='Workplace setting', help_text='Workplace setting of the job')

    employment_type = models.CharField(max_length=16, choices=EmploymentTypeChoices.choices, blank=True, null=True,
                                       verbose_name='Employment type', help_text='Employment type of the job')

    annual_salary_min = models.PositiveIntegerField(blank=True, null=True, verbose_name='Annual salary min',
                                                    help_text='Minimum annual salary of the job')

    annual_salary_max = models.PositiveIntegerField(blank=True, null=True, verbose_name='Annual salary max',
                                                    help_text='Maximum annual salary of the job')

    currency = models.CharField(max_length=16, blank=True, null=True, verbose_name='Currency',
                                help_text='Currency of the salary')

    is_promoted = models.BooleanField(default=False, verbose_name='Is promoted',
                                      help_text='Whether the job is promoted or not')

    promotion_start_date = models.DateField(blank=True, null=True, verbose_name='Promotion start date',
                                            help_text='Date when the promotion starts')

    promotion_end_date = models.DateField(blank=True, null=True, verbose_name='Promotion end date',
                                          help_text='Date when the promotion ends')

    def clean(self):
        if self.annual_salary_min and self.annual_salary_max:
            if self.annual_salary_min > self.annual_salary_max:
                raise ValidationError('Minimum salary cannot be greater than maximum salary')

    class Meta:
        ordering = ['-posting_start_date']
        verbose_name = 'Supplier job'
        verbose_name_plural = 'Supplier jobs'
        indexes = [
            models.Index(fields=['supplier']),
            models.Index(fields=['status']),
        ]

    def __str__(self) -> str:
        return f'{self.supplier.name} - {self.name} Job {self.pk}'
