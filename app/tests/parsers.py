from unittest.mock import MagicMock, call

from currency.models import Rate, Source
from currency.tasks import parse_privatbank

from currency.tasks import parse_monobank


def test_privatbank_parser(mocker):
    initial_account = Rate.objects.count()
    privat_data = [{"ccy": "EUR", "base_ccy": "UAH", "buy": "39.26000", "sale": "40.81633"}, {"ccy": "USD", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"}]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: privat_data
        )
    )
    parse_privatbank()
    assert Rate.objects.count() == initial_account + 2

    parse_privatbank()
    assert Rate.objects.count() == initial_account + 2

    assert request_get_mock.call_count == 2

    assert request_get_mock.call_args == call('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')


def test_monobank_parser(mocker):
    initial_account = Source.objects.count()
    mono_data = [{"currencyCodeA": 840, "currencyCodeB": 980, "date": 1685311274, "rateBuy": 36.65, "rateCross": 0, "rateSell": 37.4406}, {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1685374806, "rateBuy": 39.26, "rateCross": 0, "rateSell": 40.4596}]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: mono_data
        )
        )
    parse_monobank()
    assert Source.objects.count() == initial_account + 1

    parse_monobank()
    assert Source.objects.count() == initial_account + 1

    assert request_get_mock.call_count == 2

    assert request_get_mock.call_args == call('https://api.monobank.ua/bank/currency')
