# Generated by Django 5.0.4 on 2024-12-06 05:08

import apps.articles.models.article
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("supplier", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the item",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the article tag",
                        max_length=255,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Unique slug of the article tag",
                        max_length=255,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of the article tag",
                        max_length=6000,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who created the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who last modified the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article tag",
                "verbose_name_plural": "Article tags",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the item",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "date_deleted",
                    models.DateTimeField(
                        blank=True,
                        help_text="Server date and time when the item was deleted",
                        null=True,
                        verbose_name="Date deleted",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the item has been deleted or not",
                        verbose_name="Is deleted",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the article",
                        max_length=255,
                        verbose_name="Title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Unique slug of the article",
                        max_length=255,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Content of the article",
                        max_length=6000,
                        verbose_name="Content",
                    ),
                ),
                (
                    "featured_image_raw",
                    models.ImageField(
                        blank=True,
                        help_text="Raw featured image of the article",
                        null=True,
                        upload_to=apps.articles.models.article.Article.featured_image_raw_upload_path,
                        verbose_name="Featured image raw",
                    ),
                ),
                (
                    "featured_image",
                    models.ImageField(
                        blank=True,
                        help_text='Processed featured image in WEBP format.                                                <br>Required image size: 1280x1280                                                <br>Required image aspect ratio: 1.0                                                <br>The featured image should be uploaded to the "featured_image_raw" field and the model will                                                process the featured image and generate the "featured_image" and "featured_image_thumbnail" image and                                                set the value for the fields.',
                        null=True,
                        upload_to=apps.articles.models.article.Article.featured_image_processed_upload_path,
                        verbose_name="Featured image",
                    ),
                ),
                (
                    "featured_image_thumbnail",
                    models.ImageField(
                        blank=True,
                        help_text='Processed featured image thumbnail in WEBP format.                                                        <br>Required image size: 1280x1280                                                        <br>Required image aspect ratio: 1.0                                                        <br>The featured image should be uploaded to the "featured_image_raw" field and the model will                                                        process the featured image and generate the "featured_image" and "featured_image_thumbnail" image and                                                        set the value for the fields.',
                        null=True,
                        upload_to=apps.articles.models.article.Article.featured_image_processed_upload_path,
                        verbose_name="Featured image thumbnail",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("in_review", "In review"),
                            ("published", "Published"),
                            ("archived", "Archived"),
                        ],
                        default="draft",
                        help_text="Status of the article",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "visibility",
                    models.CharField(
                        choices=[
                            ("public", "Public"),
                            ("hidden", "Hidden"),
                            ("private", "Private"),
                        ],
                        default="public",
                        help_text="Visibility of the article",
                        max_length=20,
                        verbose_name="Visibility",
                    ),
                ),
                (
                    "number_of_revisions",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Number of revisions of the article",
                        verbose_name="Number of revisions",
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True,
                        help_text="Meta title of the article",
                        max_length=255,
                        null=True,
                        verbose_name="Meta title",
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True,
                        help_text="Meta description of the article",
                        max_length=6000,
                        null=True,
                        verbose_name="Meta description",
                    ),
                ),
                (
                    "meta_keywords",
                    models.CharField(
                        blank=True,
                        help_text="Meta keywords of the article",
                        max_length=255,
                        null=True,
                        verbose_name="Meta keywords",
                    ),
                ),
                (
                    "allow_comments",
                    models.BooleanField(
                        default=True,
                        help_text="Allow comments on the article",
                        verbose_name="Allow comments",
                    ),
                ),
                (
                    "allow_sharing",
                    models.BooleanField(
                        default=True,
                        help_text="Allow sharing of the article",
                        verbose_name="Allow sharing",
                    ),
                ),
                (
                    "date_published",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date the article was published",
                        null=True,
                        verbose_name="Date published",
                    ),
                ),
                (
                    "date_of_last_revision",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date of the last revision of the article",
                        null=True,
                        verbose_name="Date of last revision",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who created the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who deleted the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_deleted_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Deleted by",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who last modified the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified by",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        help_text="Tags of the article",
                        related_name="articles",
                        to="articles.articletag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
                "ordering": ["-date_modified"],
            },
        ),
        migrations.CreateModel(
            name="ContributorRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the item",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("lead_author", "Lead author"),
                            ("author", "Author"),
                            ("editor", "Editor"),
                        ],
                        help_text="Role of the contributor",
                        max_length=20,
                        verbose_name="Role",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        help_text="Article of the contributor role",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contributor_roles",
                        to="articles.article",
                        verbose_name="Article",
                    ),
                ),
                (
                    "contributor",
                    models.ForeignKey(
                        help_text="Contributor of the contributor role",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contributor_roles",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Contributor",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who created the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who last modified the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified by",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contributor role",
                "verbose_name_plural": "Contributor roles",
                "ordering": ["article"],
            },
        ),
        migrations.CreateModel(
            name="SupplierArticle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the item",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        help_text="Article of the supplier article",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_articles",
                        to="articles.article",
                        verbose_name="Article",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who created the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who last modified the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified by",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        help_text="Supplier of the supplier article",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplier_articles",
                        to="supplier.supplier",
                        verbose_name="Supplier",
                    ),
                ),
            ],
            options={
                "verbose_name": "Supplier article",
                "verbose_name_plural": "Supplier articles",
                "ordering": ["article"],
            },
        ),
        migrations.CreateModel(
            name="ArticleComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the item",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time when the item was created modified",
                        verbose_name="Date created",
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time when the item was last modified",
                        verbose_name="Date modified",
                    ),
                ),
                (
                    "date_deleted",
                    models.DateTimeField(
                        blank=True,
                        help_text="Server date and time when the item was deleted",
                        null=True,
                        verbose_name="Date deleted",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the item has been deleted or not",
                        verbose_name="Is deleted",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Content of the comment",
                        max_length=6000,
                        verbose_name="Content",
                    ),
                ),
                (
                    "is_edited",
                    models.BooleanField(
                        default=False,
                        help_text="Is the comment edited",
                        verbose_name="Is edited",
                    ),
                ),
                (
                    "is_flagged",
                    models.BooleanField(
                        default=False,
                        help_text="Is the comment flagged",
                        verbose_name="Is flagged",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        help_text="Article of the comment",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="articles.article",
                        verbose_name="Article",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who created the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who deleted the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_deleted_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Deleted by",
                    ),
                ),
                (
                    "down_votes",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Users who down voted the comment",
                        related_name="down_voted_comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Down votes",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who last modified the item",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Modified by",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        help_text="Parent of the comment",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="articles.articlecomment",
                        verbose_name="Parent",
                    ),
                ),
                (
                    "up_votes",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Users who up voted the comment",
                        related_name="up_voted_comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Up votes",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User of the comment",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article comment",
                "verbose_name_plural": "Article comments",
                "ordering": ["date_created"],
                "indexes": [
                    models.Index(
                        fields=["article"], name="articles_ar_article_1ef1e9_idx"
                    )
                ],
            },
        ),
        migrations.AddIndex(
            model_name="articletag",
            index=models.Index(fields=["name"], name="articles_ar_name_6b7ff8_idx"),
        ),
        migrations.AddIndex(
            model_name="articletag",
            index=models.Index(fields=["slug"], name="articles_ar_slug_23be95_idx"),
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(fields=["title"], name="articles_ar_title_ee81af_idx"),
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(fields=["slug"], name="articles_ar_slug_452037_idx"),
        ),
        migrations.AddIndex(
            model_name="contributorrole",
            index=models.Index(
                fields=["article"], name="articles_co_article_ab04a7_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="supplierarticle",
            index=models.Index(
                fields=["article"], name="articles_su_article_3d03f6_idx"
            ),
        ),
    ]
