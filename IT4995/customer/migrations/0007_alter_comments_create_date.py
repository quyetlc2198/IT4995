# Generated by Django 3.2 on 2021-05-26 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20210524_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 5, 26)),
        ),
    ]