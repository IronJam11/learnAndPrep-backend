# Generated by Django 5.0.6 on 2024-06-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockTest', '0003_alter_testquestionattempt_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image_test',
            field=models.URLField(max_length=128, null=True),
        ),
    ]
