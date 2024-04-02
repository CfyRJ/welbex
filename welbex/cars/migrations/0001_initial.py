# Generated by Django 5.0.3 on 2024-04-02 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=5, unique=True, verbose_name='Car number')),
                ('lifting_capacity', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations_cars', to='location.locations', verbose_name='Location')),
            ],
        ),
    ]