# Generated by Django 3.2.15 on 2022-10-09 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_bookingstatus_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingstatus',
            name='mode',
        ),
    ]