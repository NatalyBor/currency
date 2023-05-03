
from celery import shared_task
from django.conf import settings
from currency.choices import RateCurrencyChoices
import requests
from currency.constants import PRIVATBANK_CODE_NAME
from currency.constants import MONOBANK_CODE_NAME

from app.currency.utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source
    # source = Source.objects.filter(code_name=PRIVATBANK_CODE_NAME).first()
    #
    # if source is None:
    #     source = Source.objects.create(code_name=PRIVATBANK_CODE_NAME)

    source, _ = Source.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={'name': 'PrivatBank'})

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue
        buy = to_2_places_decimal(rate['buy'])
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ).order_by('-created').last()

        if last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source)


@shared_task
def parse_monobank():
    from currency.models import Source, Rate
    source = Source.objects.filter(code_name=MONOBANK_CODE_NAME).first()
    if source is None:
        source = Source.objects.create(code_name=MONOBANK_CODE_NAME)

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        840: RateCurrencyChoices.USD,
        978: RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate["currencyCodeA"] not in available_currency or rate["currencyCodeB"] != 980:
            continue
        buy = rate["rateBuy"]
        sale = rate["rateSell"]
        currency = rate["currencyCodeA"]

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ).order_by('-created').last()

        if last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


@shared_task(autoretry_for=(ConnectionError,), retry_kwargs={'max_retries': 5})
# def debug():
# 	print('DEBUG\n' * 10)
# 	from time import sleep
# 	sleep(10)
def send_mail(subject, message):
    raise ConnectionError
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )
