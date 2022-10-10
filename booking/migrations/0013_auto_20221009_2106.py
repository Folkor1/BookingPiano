# Generated by Django 3.2.15 on 2022-10-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_alter_bookingstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingstatus',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='bookingstatus',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]