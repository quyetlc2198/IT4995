# Generated by Django 3.2 on 2021-05-19 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_comments_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 5, 19)),
        ),
    ]