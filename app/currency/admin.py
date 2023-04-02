from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter

from currency.models import Rate, Source, ContactUs


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'created',
        'currency',
        'source',
    )
    list_filter = (
        'currency',
        ('created', DateRangeFilter)
    )
    search_fields = (
        'source',
        'buy',
        'sell',
    )
    # readonly_fields = (
    #     'buy',
    #     'sell',
    # )

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name'
    )


@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'email',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
