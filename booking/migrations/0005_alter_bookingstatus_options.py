# Generated by Django 3.2.15 on 2022-10-06 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_bookings_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingstatus',
            options={'verbose_name': 'Booking status'},
        ),
    ]