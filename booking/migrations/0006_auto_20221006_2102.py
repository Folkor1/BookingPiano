# Generated by Django 3.2.15 on 2022-10-06 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_bookingstatus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'Abouts'},
        ),
        migrations.AlterModelOptions(
            name='bookingstatus',
            options={'verbose_name': 'Booking status', 'verbose_name_plural': 'Booking statuses'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='lessontype',
            options={'verbose_name': 'Lesson type', 'verbose_name_plural': 'Lesson types'},
        ),
    ]
