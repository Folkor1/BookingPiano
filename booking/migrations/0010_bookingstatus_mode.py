# Generated by Django 3.2.15 on 2022-10-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20221009_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingstatus',
            name='mode',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
