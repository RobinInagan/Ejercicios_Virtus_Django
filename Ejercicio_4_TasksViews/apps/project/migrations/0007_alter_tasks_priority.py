# Generated by Django 5.0.3 on 2024-04-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_tasks_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], default=3, max_length=6),
        ),
    ]
