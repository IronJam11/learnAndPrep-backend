# Generated by Django 5.0.6 on 2024-05-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_topic_subject_id_alter_question_topic_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='solved_questions',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='total_questions',
            field=models.IntegerField(null=True),
        ),
    ]
