# Generated by Django 4.1.5 on 2023-06-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_task_completed_alter_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]