# Generated by Django 5.1 on 2024-08-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quiz_question_alter_quiz_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(max_length=200, verbose_name='Questiond'),
        ),
    ]