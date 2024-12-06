from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.core.models import BaseModel


# Models
class Country(BaseModel):
    """
    Represents a country with essential details.

    Notes:
        - May want to include a field for currency and think about how to handle multiple currencies. This may be
        useful for users that reference pricing information of uploaded products.
        - Country ISO codes can be found at: https://www.iso.org/obp/ui

    Attributes:
    - name (CharField): The official name of the country.
    - slug (SlugField): A slug field version of the country's name.
    - country_code (CharField): The standard code representation of the country (e.g., "US" for the United States,
    "UK" for the United Kingdom).
    - phone_code (IntegerField): The international phone code associated with the country (e.g., 1 for the US, 44 for
    the UK).
    - flag (ImageField): An image representing the flag of the country.

    Meta:
    - ordering: Specifies the default ordering for the country, which is based on its name.
    - verbose_name: Human-readable singular form of the object.
    - verbose_name_plural: Human-readable plural form of the object.

    Methods:
    - __str__(): Returns a string representation of the country in the format: "Name (Country Code)".
    """
    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the country')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug',
                            help_text='The slug based on the country name')

    iso_code_numeric = models.CharField(max_length=3, unique=True, verbose_name='ISO code numeric',
                                        help_text='ISO code numeric of the country')

    iso_code_alpha2 = models.CharField(max_length=2, unique=True, verbose_name='ISO code alpha 2',
                                       help_text='ISO code alpha-2 of the country')

    iso_code_alpha3 = models.CharField(max_length=3, unique=True, verbose_name='ISO code alpha 3',
                                       help_text='ISO code alpha-3 of the country')

    phone_code = models.PositiveIntegerField(verbose_name='Phone code',
                                             help_text='Phone code of the country (e.g., 1, 44, etc...)')

    flag = models.ImageField(upload_to='flags', blank=True, null=True, verbose_name='Flag',
                             help_text='Flag of the country')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.name} ({self.iso_code_alpha2})'


@receiver(pre_save, sender=Country)
def set_slug(sender, instance, *args, **kwargs):
    # Update the slug if the object is new or the object's name field has changed.
    if not instance.pk or (instance.pk and Country.objects.get(pk=instance.pk).name != instance.name):
        instance.slug = slugify(instance.name)
