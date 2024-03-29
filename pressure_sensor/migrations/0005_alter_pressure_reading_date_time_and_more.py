# Generated by Django 5.0.3 on 2024-03-08 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pressure_sensor', '0004_alter_pressure_reading_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressure_reading',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 16, 9, 2, 20471), verbose_name='installation date'),
        ),
        migrations.AlterField(
            model_name='pressure_sensor',
            name='installation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 16, 9, 2, 20471), verbose_name='installation date'),
        ),
    ]
