# Register your models here.
from apps.accounts.models import Account, AccountInteraction, AccountSettings
from apps.core.utils import AdminExportMixin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Admin objects
@admin.register(Account)
class AccountAdmin(UserAdmin, AdminExportMixin):
    list_display = ['email', 'username', 'is_staff', 'is_admin', 'is_superuser', 'date_created', 'date_last_logged_in']

    list_filter = ['is_email_verified', 'is_admin', 'is_staff', 'is_deleted']

    filter_horizontal = []

    search_fields = ['email', 'username']

    autocomplete_fields = ['country']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'short_uuid', 'email_verification_token', 'date_last_logged_in', 'date_created']

    fieldsets = [
        ('Identity', {
            'fields': ['email', 'username', 'first_name', 'last_name', 'country'],
            'description': 'General account information'
        }),
        ('Details', {
            'fields': ['profile_image_raw', 'profile_image_raw_hash', 'profile_image', 'profile_image_thumbnail', 'bio', 'organization', 'position'],
            'description': 'Account specific details'
        }),
        ('Email verification', {
            'fields': ['is_email_verified', 'email_verification_token', 'email_verification_token_expiration_date'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['is_active', 'is_staff', 'is_admin', 'is_superuser'],
            'description': 'Fields related to the property tag'
        }),
        ('System properties', {
            'fields': ['is_deleted', 'date_deleted'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'short_uuid', 'date_created', 'date_last_logged_in'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        }),
        ('Notes', {
            'fields': [],
            'description': '''
                <b>Additional properties:</b><br>
                - full_name: Returns the full name of the user (first_name + last_name)<br>
            '''
        })
    ]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )


@admin.register(AccountSettings)
class AccountSettingsAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'account', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['account__username', 'account__email']

    autocomplete_fields = ['account']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Account', {
            'fields': ['account'],
            'description': 'Account associated with the settings'
        }),
        ('General settings', {
            'fields': ['theme', 'is_profile_public', 'show_email'],
            'description': 'Settings related to the account'
        }),
        ('Email settings', {
            'fields': ['receive_marketing_emails', 'receive_weekly_digest_emails', 'receive_discovery_emails',
                       'receive_site_update_emails'],
            'description': 'Type of emails the user will receive'
        }),
        ('Notification settings', {
            'fields': ['receive_inbox_message_notifications', 'receive_announcement_notifications'],
            'description': 'Type of notifications the user will receive'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(AccountInteraction)
class AccountInteractionAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'account', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['account__username', 'account__email']

    autocomplete_fields = ['account']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Account', {
            'fields': ['account'],
            'description': 'Account associated with the interaction'
        }),
        ('Social properties', {
            'fields': ['followers', 'following'],
            'description': 'Account followers and following'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]
