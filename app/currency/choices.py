# CURRENCY_USD = 1
# CURRENCY_EUR = 2
# CURRENCY_TYPE = [
# 	(CURRENCY_USD, 'Dollar'),
# 	(CURRENCY_EUR, 'Euro'),
# ]
from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'
