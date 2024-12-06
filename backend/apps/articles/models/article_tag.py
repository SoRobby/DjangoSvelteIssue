from apps.core.models import UserTrackingModel
from django.db import models


# Model
class ArticleTag(UserTrackingModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name',
                            help_text='Name of the article tag')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug',
                            help_text='Unique slug of the article tag')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the article tag')

    class Meta:
        ordering = ['name']
        verbose_name = 'Article tag'
        verbose_name_plural = 'Article tags'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name
