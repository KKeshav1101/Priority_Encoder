# Generated by Django 5.1.4 on 2024-12-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0003_task_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]