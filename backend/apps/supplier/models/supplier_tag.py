from django.db import models

from apps.core.models import BaseModel


class SupplierTag(BaseModel):
    # Supplier tags are used to categorize suppliers based on their specialization
    name = models.CharField(max_length=255, verbose_name='Name', unique=True,
                            help_text='Name of the tag. The name will be converted to lowercase.')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug',
                            help_text='The slug based on the specialization tag name')

    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the supplier tag')

    class Meta:
        ordering = ['name']
        verbose_name = 'Supplier tag'
        verbose_name_plural = 'Supplier tags'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(SupplierTag, self).save(*args, **kwargs)
