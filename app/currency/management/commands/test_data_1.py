from django.core.management.base import BaseCommand
from currency.models import Source


class Command(BaseCommand):
    # help = "Generates random test rates"

    def handle(self, *args, **options):
        for _ in range(50):
            base_name = str(_) + 'Bank'
            Source.objects.create(
                source_url=base_name + '@example.com',
                name=base_name,
                code_name=base_name.lower()
            )
