# Generated by Django 3.2.15 on 2022-10-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_auto_20221014_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='time',
            field=models.TimeField(),
        ),
    ]
