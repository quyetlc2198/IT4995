# Generated by Django 3.2 on 2021-05-27 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20210527_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='voucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.voucher'),
        ),
    ]
