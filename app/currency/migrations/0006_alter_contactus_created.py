# Generated by Django 4.1.7 on 2023-03-12 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_rename_email_from_contactus_email_contactus_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 12, 18, 12, 33, 173981, tzinfo=datetime.timezone.utc)),
        ),
    ]
