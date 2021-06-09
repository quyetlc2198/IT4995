# Generated by Django 3.2 on 2021-06-08 02:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('discount', models.FloatField(default=0)),
                ('qty', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=100, null=True)),
                ('create_date', models.DateField(default=datetime.date(2021, 6, 8))),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='price',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRM', 'Confirm'), ('OCCUPIED', 'Occupied'), ('RETURNED', 'Returned'), ('CANCEL', 'Cancel')], default='PENDING', max_length=10),
        ),
        migrations.AddField(
            model_name='categories',
            name='description_home',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(default='', upload_to='static/images/categories'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='image',
            field=models.ImageField(upload_to='static/images/rooms'),
        ),
        migrations.AddField(
            model_name='booking',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.voucher'),
        ),
    ]
