# Generated by Django 3.2 on 2021-05-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_rooms_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRM', 'Confirm')], default='PENDING', max_length=10),
        ),
    ]
