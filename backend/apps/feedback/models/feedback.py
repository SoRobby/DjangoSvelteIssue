from apps.core.models import BaseModel
from config import settings
from django.db import models


# Models
class FeedbackMessage(BaseModel):
    class CategoryChoices(models.TextChoices):
        BUG = 'bug', 'Bug'
        FEATURE_REQUEST = 'feature_request', 'Feature Request'
        GENERAL = 'general', 'General'
        OTHER = 'other', 'Other'

    class StatusChoices(models.TextChoices):
        IN_REVIEW = 'in_review', 'In Review'
        PLANNED = 'planned', 'Planned'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        ARCHIVED = 'archived', 'Archived'
        REJECTED = 'rejected', 'Rejected'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='feedback_messages', verbose_name='User', help_text='User who created the feedback')

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name',
                            help_text='Name of the feedback')

    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Email',
                              help_text='Email of the feedback')

    page_url = models.URLField(max_length=255, blank=True, null=True, verbose_name='Page URL',
                               help_text='URL of the page where the feedback was created')

    category = models.CharField(max_length=255, default=CategoryChoices.GENERAL, choices=CategoryChoices.choices,
                                verbose_name='Category', help_text='Category of the feedback')

    status = models.CharField(max_length=20, default=StatusChoices.IN_REVIEW, choices=StatusChoices.choices,
                              verbose_name='Status', help_text='Status of the feedback')

    content = models.TextField(max_length=5000, verbose_name='Content', help_text='Message of the feedback')

    date_completed = models.DateTimeField(blank=True, null=True, verbose_name='Date completed',
                                          help_text='Date the feedback was completed')

    date_archived = models.DateTimeField(blank=True, null=True, verbose_name='Date archived',
                                         help_text='Date the feedback was archived')

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Feedback message'
        verbose_name_plural = 'Feedback messages'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['status']),
        ]

    def __str__(self) -> str:
        return f'Feedback message {self.pk}'



