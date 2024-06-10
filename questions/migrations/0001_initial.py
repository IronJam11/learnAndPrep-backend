# Generated by Django 5.0.6 on 2024-06-10 14:35

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.RegexValidator('^(CH)|(MA)|(PH)\\d{2}$', 'ID must be of format: Subject Letter + 2 digits')])),
                ('chapter_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(7), django.core.validators.RegexValidator('^(CH)|(MA)|(PH)\\d{5}$', 'ID must be of format: Subject Letter + 2 digits')])),
                ('type', models.CharField(choices=[('SMCQ', 'Single Option Correct'), ('MMCQ', 'Multiple Option Correct'), ('INT', 'Integer Answer Type'), ('MATCH', 'Match the Matrix'), ('COMPR', 'Comprehension')], max_length=128)),
                ('source', models.CharField(choices=[('MODULE', 'From Nucleus Module'), ('MAIN', 'Jee Mains pyq'), ('ADV', 'Jee Advance pyq'), ('TEST', 'Uploaded for mock test'), ('MISSL', 'Missl')], max_length=128)),
                ('question', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_questions', to='questions.chapter')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSmcq',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('correct_option', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('question_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_query_name='answer_smcq', to='questions.question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerMmcq',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('is_O1_correct', models.BooleanField(default=False)),
                ('is_O2_correct', models.BooleanField(default=False)),
                ('is_O3_correct', models.BooleanField(default=False)),
                ('is_O4_correct', models.BooleanField(default=False)),
                ('question_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_query_name='answer_mmcq', to='questions.question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerIntegerType',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('correct_answer', models.IntegerField()),
                ('question_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_query_name='answer_integer', to='questions.question')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.subject'),
        ),
    ]
