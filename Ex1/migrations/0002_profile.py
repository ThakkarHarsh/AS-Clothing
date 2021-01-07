# Generated by Django 3.1.3 on 2021-01-06 05:34

import Ex1.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ex1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('tel', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Enter valid phone number must be entered in the format: '+9999999999'.", regex='^+?1?d{9,15}$')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=Ex1.models.upload_image_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]