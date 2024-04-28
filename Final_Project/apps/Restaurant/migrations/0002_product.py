# Generated by Django 5.0.3 on 2024-04-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost_per_unit', models.IntegerField()),
                ('all_restaurants', models.BooleanField(default=False)),
            ],
        ),
    ]