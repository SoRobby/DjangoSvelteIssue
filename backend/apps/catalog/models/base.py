from django.core.validators import RegexValidator
from django.db import models

from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from apps.properties.models import Property


class VisibilityChoices(models.TextChoices):
    normal = 'normal', 'Normal'
    hidden = 'hidden', 'Hidden'
    admin = 'admin', 'Admin'


class StatusChoices(models.TextChoices):
    draft = 'draft', 'Draft'
    published = 'published', 'Published'
    archived = 'archived', 'Archived'


