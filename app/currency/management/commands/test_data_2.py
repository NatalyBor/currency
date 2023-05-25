from django.core.management.base import BaseCommand
from currency.models import ContactUs
import random


class Command(BaseCommand):
    # help = "Generates random contact us "
    name_choices = ['Igor', 'Mike', 'Mary', 'Nataly']

    def handle(self, *args, **options):
        for _ in range(50):
            name = random.choice(self.name_choices)
            ContactUs.objects.create(
                name=name,
                subject=name + 'is writing you',
                email=name + '@example.com',
                message=f'Congratulations from {name}'
            )
