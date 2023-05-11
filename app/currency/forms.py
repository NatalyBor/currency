from django import forms

from currency.models import Rate, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'source',
            'currency',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'code_name',
        )
