# Generated by Django 4.1.5 on 2023-06-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_completed_task_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]