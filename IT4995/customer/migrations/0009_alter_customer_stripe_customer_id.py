# Generated by Django 3.2 on 2021-05-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20210526_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(default='', max_length=120),
        ),
    ]