# Generated by Django 3.2.15 on 2022-10-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_auto_20221010_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingstatus',
            name='status',
            field=models.IntegerField(choices=[(0, 'Completed'), (1, 'Upcoming')], default=0),
        ),
    ]
