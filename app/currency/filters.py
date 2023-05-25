import django_filters

from currency.models import Rate, Source, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sale': ('gt', 'gte', 'lt', 'lte', 'exact'),
        }


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ['name', 'code_name']


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = ['name', 'subject']
