# Generated by Django 4.0.1 on 2022-01-28 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_answer_question_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
    ]
