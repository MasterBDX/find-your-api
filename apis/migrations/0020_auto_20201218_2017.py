# Generated by Django 3.1.2 on 2020-12-18 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0019_auto_20201218_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentapimodel',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='postapimodel',
            name='published_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]