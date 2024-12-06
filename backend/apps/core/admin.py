from apps.core.utils import AdminExportMixin
from django.contrib import admin

from .models import Country, SubnationalRegion


# Admin objects
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'slug', 'iso_code_alpha3', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name', 'slug', 'iso_code_alpha2', 'iso_code_alpha3', 'iso_code_numeric']

    autocomplete_fields = []

    prepopulated_fields = {'slug': ['name']}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Country', {
            'fields': ['name', 'slug', 'phone_code', 'flag'],
            'description': 'Primary country fields and properties'
        }),
        ('ISO codes', {
            'fields': ['iso_code_alpha2', 'iso_code_alpha3', 'iso_code_numeric'],
            'description': 'ISO codes for country identification'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        }),
        ('Notes', {
            'fields': [],
            'description': '''
                <b>References:</b><br>
                - Country ISO codes: https://www.iso.org/obp/ui<br>
            '''
        })
    ]


@admin.register(SubnationalRegion)
class SubnationalRegionAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'slug', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name', 'slug', 'country__name', 'country__slug']

    autocomplete_fields = ['country']

    prepopulated_fields = {'slug': ['name']}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Subnational region', {
            'fields': ['country', 'name', 'slug'],
            'description': 'Subnational region fields and properties. A subnational region is a region like a state,\
            province, or territory within a country.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]

