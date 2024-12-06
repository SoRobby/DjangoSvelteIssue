import os

from django.db import models

from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from .article_tag import ArticleTag


# Model
class Article(UserTrackingModel, SoftDeletionWithUserModel):
    FEATURED_IMAGE_ASPECT_RATIO = 1 / 1
    FEATURED_IMAGE_SIZE = (1280, 1280)
    FEATURED_IMAGE_THUMBNAIL_SIZE = (128, 128)

    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        IN_REVIEW = 'in_review', 'In review'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    class VisibilityChoices(models.TextChoices):
        PUBLIC = 'public', 'Public'
        HIDDEN = 'hidden', 'Hidden'
        PRIVATE = 'private', 'Private'

    def featured_image_raw_upload_path(self, filename):
        extension = os.path.splitext(filename)[1]
        return f'articles/{self.uuid}/featured-image/raw{extension}'

    def featured_image_processed_upload_path(self, filename):
        return f'articles/{self.uuid}/featured-image/profile-image.webp'

    def featured_image_thumbnail_processed_upload_path(self, filename):
        return f'articles/{self.uuid}/featured-image/thumbnail.webp'

    title = models.CharField(max_length=255, verbose_name='Title', help_text='Title of the article')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug', help_text='Unique slug of the article')

    tags = models.ManyToManyField(ArticleTag, related_name='articles', verbose_name='Tags',
                                  help_text='Tags of the article')

    content = models.TextField(max_length=6000, verbose_name='Content', help_text='Content of the article')

    featured_image_raw = models.ImageField(upload_to=featured_image_raw_upload_path, blank=True, null=True,
                                           verbose_name='Featured image raw',
                                           help_text='Raw featured image of the article')

    featured_image = models.ImageField(upload_to=featured_image_processed_upload_path, blank=True, null=True,
                                       verbose_name='Featured image',
                                       help_text=f'Processed featured image in WEBP format.\
                                                <br>Required image size: {FEATURED_IMAGE_SIZE[0]}x{FEATURED_IMAGE_SIZE[1]}\
                                                <br>Required image aspect ratio: {FEATURED_IMAGE_ASPECT_RATIO}\
                                                <br>The featured image should be uploaded to the "featured_image_raw" field and the model will\
                                                process the featured image and generate the "featured_image" and "featured_image_thumbnail" image and\
                                                set the value for the fields.')

    featured_image_thumbnail = models.ImageField(upload_to=featured_image_processed_upload_path, blank=True,
                                                 null=True,
                                                 verbose_name='Featured image thumbnail',
                                                 help_text=f'Processed featured image thumbnail in WEBP format.\
                                                        <br>Required image size: {FEATURED_IMAGE_SIZE[0]}x{FEATURED_IMAGE_SIZE[1]}\
                                                        <br>Required image aspect ratio: {FEATURED_IMAGE_ASPECT_RATIO}\
                                                        <br>The featured image should be uploaded to the "featured_image_raw" field and the model will\
                                                        process the featured image and generate the "featured_image" and "featured_image_thumbnail" image and\
                                                        set the value for the fields.')

    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT,
                              verbose_name='Status', help_text='Status of the article')

    visibility = models.CharField(max_length=20, choices=VisibilityChoices.choices, default=VisibilityChoices.PUBLIC,
                                  verbose_name='Visibility', help_text='Visibility of the article')

    number_of_revisions = models.PositiveIntegerField(default=0, verbose_name='Number of revisions',
                                                      help_text='Number of revisions of the article')

    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Meta title',
                                  help_text='Meta title of the article')

    meta_description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Meta description',
                                        help_text='Meta description of the article')

    meta_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name='Meta keywords',
                                     help_text='Meta keywords of the article')

    allow_comments = models.BooleanField(default=True, verbose_name='Allow comments',
                                         help_text='Allow comments on the article')

    allow_sharing = models.BooleanField(default=True, verbose_name='Allow sharing',
                                        help_text='Allow sharing of the article')

    date_published = models.DateTimeField(blank=True, null=True, verbose_name='Date published',
                                          help_text='Date the article was published')

    date_of_last_revision = models.DateTimeField(blank=True, null=True, verbose_name='Date of last revision',
                                                 help_text='Date of the last revision of the article')

    class Meta:
        ordering = ['-date_modified']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['slug']),
        ]
