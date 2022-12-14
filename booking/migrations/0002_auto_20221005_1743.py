# Generated by Django 3.2.15 on 2022-10-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('date', 'time')},
        ),
    ]
