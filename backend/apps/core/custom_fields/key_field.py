from django.core.validators import RegexValidator
from django.db import models

"""
# Original field that was used across many different models
# key = models.CharField(max_length=255, verbose_name='Key', unique=True,
#                        help_text='Key of the taxonomy, used for API calls',
#                        validators=[RegexValidator(regex='^[a-z_][a-z0-9_]*$',
#                                                   message='Key must be lowercase, cannot start with a number, and\
#                                                   can only contain underscores.')])
"""


class KeyField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 255)
        kwargs.setdefault('verbose_name', 'Key')
        kwargs.setdefault('unique', True)
        kwargs.setdefault('help_text', 'Key used for API calls')
        kwargs.setdefault('validators', [
            RegexValidator(
                regex='^[a-z_][a-z0-9_]*$',
                message='Key must be lowercase, cannot start with a number, and can only contain underscores.'
            )
        ])
        super().__init__(*args, **kwargs)
