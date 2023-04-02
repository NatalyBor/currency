# Generated by Django 4.1.7 on 2023-03-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')]),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
