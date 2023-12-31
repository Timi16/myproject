# Generated by Django 4.0 on 2023-07-25 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_worker_city_worker_country_worker_profile_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='profile_picture',
        ),
        migrations.AlterField(
            model_name='worker',
            name='availability',
            field=models.CharField(choices=[('full_time', 'Full-Time'), ('part_time', 'Part-Time'), ('contract', 'Contract')], max_length=100),
        ),
    ]
