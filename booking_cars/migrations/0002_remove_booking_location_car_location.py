# Generated by Django 5.2.1 on 2025-06-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='location',
        ),
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.TextField(default='Kiev'),
        ),
    ]
