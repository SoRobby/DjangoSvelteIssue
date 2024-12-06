import hashlib
import logging
import os
from io import BytesIO
from uuid import uuid4

from apps.accounts.managers import AccountManager
from apps.accounts.utils import generate_short_uuid
from apps.core.models import Country
from django.contrib.auth.models import AbstractBaseUser
from django.core.files.base import ContentFile
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image


# Models
class Account(AbstractBaseUser):
    # TODO - Add field of organization

    PROFILE_IMAGE_ASPECT_RATIO = 1 / 1
    PROFILE_IMAGE_SIZE = (640, 640)
    PROFILE_IMAGE_THUMBNAIL_SIZE = (128, 128)

    def profile_image_raw_upload_path(self, filename) -> str:
        extension = os.path.splitext(filename)[1]
        return f'accounts/{self.uuid}/profile-image/raw{extension}'

    def profile_image_processed_upload_path(self, filename) -> str:
        return f'accounts/{self.uuid}/profile-image/profile-image.webp'

    def profile_image_thumbnail_processed_upload_path(self, filename) -> str:
        return f'accounts/{self.uuid}/profile-image/thumbnail.webp'

    email = models.EmailField(max_length=255, unique=True, verbose_name='Email', help_text='Unique email address')

    username = models.CharField(max_length=16, unique=True,
                                validators=[
                                    RegexValidator(regex='^[a-zA-Z0-9_]*$',
                                                   message='Username must be alphanumeric or contain any of the'
                                                           ' following: "_"',
                                                   code='invalid_username'),
                                    MinLengthValidator(limit_value=4,
                                                       message='Username must be at least 4 characters long')
                                ],
                                verbose_name='Username', help_text='Unique username associated with the account')

    first_name = models.CharField(max_length=120, blank=True, verbose_name='First name',
                                  help_text='First name of the user')

    last_name = models.CharField(max_length=120, blank=True, verbose_name='Last name',
                                 help_text='Last name of the user')

    bio = models.TextField(max_length=1000, blank=True, verbose_name='Bio', help_text='User bio')

    organization = models.CharField(max_length=255, blank=True, null=True, verbose_name='Organization', help_text='User organization')

    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='Position', help_text='User position')

    is_active = models.BooleanField(default=True, verbose_name='Active',
                                    help_text='Designates whether this user should be treated as active')

    is_staff = models.BooleanField(default=False, verbose_name='Staff status',
                                   help_text='Designates whether the user can log into this admin site')

    is_admin = models.BooleanField(default=False, verbose_name='Admin status',
                                   help_text='Designates whether the user can log into this admin site')

    is_superuser = models.BooleanField(default=False, verbose_name='Superuser status',
                                       help_text='Designates that this user has all permissions without explicitly '
                                                 'assigning them')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Country',
                                help_text='Country of the user')

    profile_image_raw = models.ImageField(upload_to=profile_image_raw_upload_path, blank=True, null=True,
                                          verbose_name='Profile image raw',
                                          help_text='Raw profile image or avatar of the account')
    
    profile_image_raw_hash = models.CharField(max_length=255, blank=True, null=True, verbose_name='Profile image raw hash', help_text='Hash of the raw profile image or avatar of the account, using the MD5 hash algorithm')

    profile_image = models.ImageField(upload_to=profile_image_processed_upload_path, blank=True, null=True,
                                      verbose_name='Profile image',
                                      help_text=f'Processed profile image in WEBP format.\
                                                <br>Required image size: {PROFILE_IMAGE_SIZE[0]}x{PROFILE_IMAGE_SIZE[1]}\
                                                <br>Required image aspect ratio: {PROFILE_IMAGE_ASPECT_RATIO}\
                                                <br>The profile image should be uploaded to the "profile_image_raw" field and the model will\
                                                process the profile image and generate the "profile_image" and "profile_image_thumbnail" image and\
                                                set the value for the fields.')

    profile_image_thumbnail = models.ImageField(upload_to=profile_image_thumbnail_processed_upload_path, blank=True,
                                                null=True,
                                                verbose_name='Profile image thumbnail',
                                                help_text=f'Processed profile image thumbnail in WEBP format.\
                                                <br>Required image size: {PROFILE_IMAGE_SIZE[0]}x{PROFILE_IMAGE_SIZE[1]}\
                                                <br>Required image aspect ratio: {PROFILE_IMAGE_ASPECT_RATIO}\
                                                <br>The profile image should be uploaded to the "profile_image_raw" field and the model will\
                                                process the profile image and generate the "profile_image" and "profile_image_thumbnail" image and\
                                                set the value for the fields.')

    is_email_verified = models.BooleanField(default=False, verbose_name='Is email verified',
                                            help_text='Designates whether the user has verified their email address')

    email_verification_token = models.UUIDField(default=uuid4, editable=True, unique=True,
                                                verbose_name='Email verification token',
                                                help_text='Unique identifier for the email verification token')

    email_verification_token_expiration_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,
                                                                    null=True,
                                                                    verbose_name='Email verification token expiration date',
                                                                    help_text='Server date and time when the email verification token expires')

    is_deleted = models.BooleanField(default=False, verbose_name='Is marked for deletion',
                                     help_text='Designates whether the user has marked their account for\
                                                 deletion')

    date_deleted = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                        verbose_name='Date marked for deletion',
                                        help_text='Server date and time when the user deleted their\
                                                    account')

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name='UUID',
                            help_text='Unique identifier for the account')

    short_uuid = models.CharField(max_length=12, unique=True, editable=False,
                                  validators=[
                                      MinLengthValidator(limit_value=12,
                                                         message='Short UUID must be exactly 12 characters long')
                                  ],
                                  verbose_name='Short UUID', help_text='Short unique identifier for the account'
                                  )

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created',
                                        help_text='Server date and time the account was created')

    date_last_logged_in = models.DateTimeField(auto_now=True, verbose_name='Date last logged in',
                                               help_text='Server date and time the account last logged in')

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        # Set the date_deleted if the post is deleted
        if self.is_deleted and self.date_deleted is None:
            self.date_deleted = timezone.now()

        # Call the original save method of models.model
        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return True

    def generate_new_email_verification_token(self):
        self.email_verification_token = uuid4()
        self.save()

    def add_profile_image_with_cropping(self, raw_image, crop_x: int, crop_y: int, crop_width: int, crop_height: int):

        # Save the raw image
        self.profile_image_raw = raw_image
        self.save()


        # Calculate hash of the raw image
        image = Image.open(raw_image)
        if image.mode in ("RGBA", "P", "LA"):
            image = image.convert('RGB')
        self.profile_image_raw_hash = hashlib.md5(image.tobytes()).hexdigest()
        
        # TODO

        # Open the image
        image = Image.open(self.profile_image_raw)

        if image.mode in ("RGBA", "P", "LA"):
            image = image.convert('RGB')

        # Crop image using Crop dimensions
        raw_image_cropped = image.crop(
            (crop_x, crop_y, crop_width + crop_x, crop_height + crop_y)
        )

        # Process the raw uploaded profile image image
        main_image = raw_image_cropped.resize(self.PROFILE_IMAGE_SIZE, Image.LANCZOS)
        main_output = BytesIO()
        main_image.save(main_output, format='WEBP')
        main_output.seek(0)
        self.profile_image.save(os.path.splitext(self.profile_image_raw.name)[0] + '.webp',
                                ContentFile(main_output.read()), save=False)

        # Process the thumbnail image
        thumbnail_image = raw_image_cropped.resize(self.PROFILE_IMAGE_THUMBNAIL_SIZE, Image.LANCZOS)
        thumbnail_output = BytesIO()
        thumbnail_image.save(thumbnail_output, format='WEBP')
        thumbnail_output.seek(0)
        self.profile_image_thumbnail.save(os.path.splitext(self.profile_image_raw.name)[0] + '_thumbnail.webp',
                                          ContentFile(thumbnail_output.read()), save=False)


        # self.profile_image_raw_hash = hashlib.md5(raw_image.tobytes()).hexdigest()

    # def process_and_save_profile_image(self):
    #     # Ref> https://chat.openai.com/share/02479099-4516-4217-ac11-5e4e1e1e7a57
    #     if not self.profile_image_raw:
    #         return

    #     image = Image.open(self.profile_image_raw)

    #     if image.mode in ("RGBA", "P", "LA"):
    #         image = image.convert('RGB')

    #     # Process the raw uploaded profile image image
    #     main_image = image.resize(self.PROFILE_IMAGE_SIZE, Image.LANCZOS)
    #     main_output = BytesIO()
    #     main_image.save(main_output, format='WEBP')
    #     main_output.seek(0)
    #     self.profile_image.save(os.path.splitext(self.profile_image_raw.name)[0] + '.webp',
    #                             ContentFile(main_output.read()), save=False)

    #     # Process the thumbnail image
    #     thumbnail_image = image.resize(self.PROFILE_IMAGE_THUMBNAIL_SIZE, Image.LANCZOS)
    #     thumbnail_output = BytesIO()
    #     thumbnail_image.save(thumbnail_output, format='WEBP')
    #     thumbnail_output.seek(0)
    #     self.profile_image_thumbnail.save(os.path.splitext(self.profile_image_raw.name)[0] + '_thumbnail.webp',
    #                                       ContentFile(thumbnail_output.read()), save=False)

    @property
    def theme_choices_as_list(self):
        return [{'key': key, 'name': name} for i, (key, name) in enumerate(self.ThemeChoices.choices)]

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        else:
            return self.username

    @staticmethod
    def get_theme_choices_as_dict():
        return dict(Account.ThemeChoices.choices)

    @staticmethod
    def get_theme_choices_as_list():
        """
        Returns the theme choices as a list of dictionaries with keys 'key' and 'name' for each choice.
        :return: list of dictionaries
        """
        return [{'key': key, 'name': name} for key, name in Account.ThemeChoices.choices]


class AccountSettings(models.Model):
    # Choice classes
    class ThemeChoices(models.TextChoices):
        LIGHT = 'light', 'Light'
        DARK = 'dark', 'Dark'
        SYSTEM = 'system', 'System'

    account = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name='Account', related_name='settings',
                                   help_text='Account that is connected to the settings')

    theme = models.CharField(max_length=55, default=ThemeChoices.SYSTEM, choices=ThemeChoices.choices,
                             verbose_name='Theme', help_text='User website theme')

    is_profile_public = models.BooleanField(default=True, verbose_name='Profile public',
                                            help_text='Designates whether the user profile can be viewed by others')

    show_email = models.BooleanField(default=False, verbose_name='Show email', help_text='Show or hide the email')

    receive_marketing_emails = models.BooleanField(default=True, verbose_name='Marketing emails',
                                                   help_text='Receive marketing emails')

    receive_weekly_digest_emails = models.BooleanField(default=True, verbose_name='Weekly digest emails',
                                                       help_text='Receive weekly digest emails')

    receive_discovery_emails = models.BooleanField(default=True, verbose_name='Discovery emails',
                                                   help_text='Receive emails about new features and tips')

    receive_site_update_emails = models.BooleanField(default=True, verbose_name='Site updates',
                                                     help_text='Receive site update emails')

    receive_inbox_message_notifications = models.BooleanField(default=True, verbose_name='Inbox message notifications',
                                                              help_text='Receive notifications when you receive a new\
                                                              message in your inbox')

    receive_announcement_notifications = models.BooleanField(default=True, verbose_name='Announcement notifications',
                                                             help_text='Receive notifications about new announcements')

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name='UUID',
                            help_text='Unique identifier for the account settings')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created',
                                        help_text='Server date and time when the item was created modified')

    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified',
                                         help_text='Server date and time when the item was last modified')

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Account setting'
        verbose_name_plural = 'Account settings'

    def __str__(self) -> str:
        return f"{self.account.username} settings"


class AccountInteraction(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name='Account',
                                   related_name='interactions', help_text='Account that is connected to the settings')

    followers = models.ManyToManyField(Account, verbose_name='Followers', related_name='following',
                                       help_text='Accounts that are following this account')

    following = models.ManyToManyField(Account, verbose_name='Following', related_name='followers',
                                       help_text='Accounts that this account is following')

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name='UUID',
                            help_text='Unique identifier for the account settings')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created',
                                        help_text='Server date and time when the item was created modified')

    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified',
                                         help_text='Server date and time when the item was last modified')

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Account interaction'
        verbose_name_plural = 'Account interactions'

    def __str__(self) -> str:
        return f"{self.account.username} interactions"


# class AccountApiKeys(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account',
#                                 related_name='api_keys', help_text='Account that is connected to the API keys')
    
#     name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the API key')

#     key = models.CharField(max_length=255, unique=True, verbose_name='API key',
#                            help_text='Unique API key for the account')
    
#     is_active = models.BooleanField(default=True, verbose_name='Active',
#                                     help_text='Designates whether this API key should be treated as active')

#     date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created',
#                                         help_text='Server date and time when the API key was created')

#     date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified',
#                                          help_text='Server date and time when the API key was last modified')

#     class Meta:
#         ordering = ['-date_created']
#         verbose_name = 'Account API key'
#         verbose_name_plural = 'Account API keys'

#     def __str__(self) -> str:
#         return f"{self.account.username} API key"


# Model signals
@receiver(pre_save, sender=Account)
def pre_save_account(sender, instance, *args, **kwargs):
    if not instance.short_uuid:
        instance.short_uuid = generate_short_uuid(instance, length=instance._meta.get_field('short_uuid').max_length)

    # # Process profile images
    # if instance.pk:
    #     old_instance = Account.objects.get(pk=instance.pk)

    #     # Check to see if a new profile image has been uploaded
    #     if old_instance.profile_image_raw != instance.profile_image_raw:

    #         # Delete the old profile image
    #         if old_instance.profile_image_raw:
    #             old_instance.profile_image_raw.delete(save=False)
    #         if old_instance.profile_image:
    #             old_instance.profile_image.delete(save=False)
    #         if old_instance.profile_image_thumbnail:
    #             old_instance.profile_image_thumbnail.delete(save=False)

    #         # Process and save new images
    #         instance.process_and_save_profile_image()

    # else:
    #     instance.process_and_save_profile_image()


@receiver(post_save, sender=Account)
def setup_account_tables(sender, instance, created, **kwargs):
    if created:
        AccountSettings.objects.create(account=instance)
        AccountInteraction.objects.create(account=instance)


@receiver(post_delete, sender=Account)
def post_delete_supplier(sender, instance, **kwargs):
    if instance.profile_image_raw:
        instance.profile_image_raw.delete(False)
    if instance.profile_image:
        instance.profile_image.delete(False)
    if instance.profile_image_thumbnail:
        instance.profile_image_thumbnail.delete(False)
