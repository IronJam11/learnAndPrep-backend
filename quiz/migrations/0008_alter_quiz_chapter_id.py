# Generated by Django 5.0.6 on 2024-06-25 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_alter_answerintegertype_question_id_and_more'),
        ('quiz', '0007_quizquestionattemptint_answer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='chapter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.chapter'),
        ),
    ]