# Generated by Django 4.0.1 on 2022-01-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='body',
            field=models.TextField(null=True),
        ),
    ]