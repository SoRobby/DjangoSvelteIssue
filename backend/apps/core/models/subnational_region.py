from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.core.models import BaseModel
from .countries import Country


# Models
class SubnationalRegion(BaseModel):
    """
    Represents a country with essential details.
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='subnational_regions',
                                verbose_name='Country', help_text='Country of the subnational region')

    name = models.CharField(max_length=255, verbose_name='Name',
                            help_text='Name of the subnational region (aka state/province/region)')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug',
                            help_text='The slug based on the country name')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Subnational Region'
        verbose_name_plural = 'Subnational Regions'

    def __str__(self):
        return f'{self.name}'


@receiver(pre_save, sender=SubnationalRegion)
def set_slug(sender, instance, *args, **kwargs):
    # Update the slug if the object is new or the object's name field has changed.
    if not instance.pk or (instance.pk and SubnationalRegion.objects.get(pk=instance.pk).name != instance.name):
        instance.slug = slugify(instance.name)
