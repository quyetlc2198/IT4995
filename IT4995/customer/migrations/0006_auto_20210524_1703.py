# Generated by Django 3.2 on 2021-05-24 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_comments_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 5, 24)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
    ]