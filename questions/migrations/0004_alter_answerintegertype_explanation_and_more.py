# Generated by Django 5.0.6 on 2024-06-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerintegertype',
            name='explanation',
            field=models.ImageField(null=True, upload_to='explanations/'),
        ),
        migrations.AlterField(
            model_name='answermmcq',
            name='explanation',
            field=models.ImageField(null=True, upload_to='explanations/'),
        ),
        migrations.AlterField(
            model_name='answersmcq',
            name='explanation',
            field=models.ImageField(null=True, upload_to='explanations/'),
        ),
    ]