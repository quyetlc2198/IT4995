# Generated by Django 3.2 on 2021-05-27 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_customer_stripe_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 5, 27)),
        ),
    ]
