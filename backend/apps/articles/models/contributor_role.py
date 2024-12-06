from django.db import models

from apps.core.models import UserTrackingModel
from config import settings
from .article import Article


# Model
class ContributorRole(UserTrackingModel):
    class RoleChoices(models.TextChoices):
        LEAD_AUTHOR = 'lead_author', 'Lead author'
        AUTHOR = 'author', 'Author'
        EDITOR = 'editor', 'Editor'

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='contributor_roles',
                                verbose_name='Article', help_text='Article of the contributor role')

    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='contributor_roles', verbose_name='Contributor',
                                    help_text='Contributor of the contributor role')

    role = models.CharField(max_length=20, choices=RoleChoices.choices, verbose_name='Role',
                            help_text='Role of the contributor')

    class Meta:
        ordering = ['article']
        verbose_name = 'Contributor role'
        verbose_name_plural = 'Contributor roles'
        indexes = [
            models.Index(fields=['article'])
        ]

    def __str__(self):
        return f'{self.article.title} - {self.contributor.name} ({self.role})'
