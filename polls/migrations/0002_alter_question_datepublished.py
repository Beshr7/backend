# Generated by Django 5.0.3 on 2024-04-01 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 2, 0, 49, 47, 68785), verbose_name='Date Published'),
        ),
    ]
