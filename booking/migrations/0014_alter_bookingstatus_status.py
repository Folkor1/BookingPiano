# Generated by Django 3.2.15 on 2022-10-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20221009_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingstatus',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
