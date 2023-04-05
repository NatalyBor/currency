from django.db import models

from currency.choices import RateCurrencyChoices

from django.utils import timezone


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )  # usd, eur
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    #source = models.CharField(max_length=25)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}'


class ContactUs(models.Model):
    created = models.DateTimeField(default=timezone.now())
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=256)
    message = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=16)
    # time = models.DateTimeField()
    time = models.IntegerField()

    def __str__(self):
        return f"Path: {self.path} | Method: {self.request_method} | Time: {self.time} ms"
