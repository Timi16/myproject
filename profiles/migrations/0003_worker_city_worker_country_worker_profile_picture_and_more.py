# Generated by Django 4.0 on 2023-07-25 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_employer_profile_visibility_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='worker',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='worker',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='worker',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_text', models.TextField()),
                ('resume', models.FileField(blank=True, null=True, upload_to='job_applications/resumes/')),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='profiles.jobposting')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='profiles.worker')),
            ],
        ),
    ]
