# Generated by Django 5.0.6 on 2024-06-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockTest', '0006_alter_testquestionattempt_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestionattempt',
            name='status',
            field=models.CharField(choices=[('Skipped', 'Skipped'), ('Unattempted', 'Unattempted'), ('Attempted', 'Attempted')], max_length=64, null=True),
        ),
    ]