# Generated by Django 2.2.10 on 2021-09-12 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_of_last_service',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 11, 22, 57, 28, 645597)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date_of_purchase',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 11, 22, 57, 28, 645597)),
        ),
    ]
