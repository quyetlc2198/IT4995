# Generated by Django 3.2 on 2021-05-28 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_alter_booking_voucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 5, 28)),
        ),
    ]
