# Generated by Django 5.0.6 on 2024-06-07 12:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.RegexValidator('^(CH|MA|PH)\\d{4}$', 'ID must be of format: Subject Letter (CH, MA, or PH) + 4 digits')]),
        ),
    ]
