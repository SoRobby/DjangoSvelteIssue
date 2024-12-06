from apps.core.models import BaseModel
from config import settings
from django.db import models
from django.utils import timezone


class SupportMessage(BaseModel):
    class StatusChoices(models.TextChoices):
        NOT_STARTED = 'not_started', 'Not Started'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='support_messages', verbose_name='User',
                             help_text='User who submitted the support message')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the person who submitted the support message')

    email = models.EmailField(max_length=255, verbose_name='Email', help_text='Email of the person who submitted the support message')

    page_url = models.URLField(max_length=255, blank=True, null=True, verbose_name='Page URL',
                               help_text='URL of the page where the support item was submitted from')

    status = models.CharField(max_length=20, default=StatusChoices.NOT_STARTED, choices=StatusChoices.choices,
                              verbose_name='Status', help_text='Status of the feedback')
    
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name='Subject', 
                               help_text='Subject of the support message')

    content = models.TextField(max_length=5000, verbose_name='Content', help_text='Message of the feedback')

    date_completed = models.DateTimeField(blank=True, null=True, verbose_name='Date completed',
                                          help_text='Date the feedback was completed')

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Support message'
        verbose_name_plural = 'Support messages'
        indexes = [
            models.Index(fields=['status']),
        ]

    def save(self, *args, **kwargs):
        if self.pk:
            support_message = SupportMessage.objects.get(pk=self.pk)

            # Check if the status has changed to "complete"
            if support_message.status in [self.StatusChoices.NOT_STARTED, self.StatusChoices.IN_PROGRESS] and self.status == self.StatusChoices.COMPLETED:
                self.date_completed = timezone.now()
            elif self.status in [self.StatusChoices.NOT_STARTED, self.StatusChoices.IN_PROGRESS] and self.date_completed:
                self.date_completed = None

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Support message {self.pk}'
