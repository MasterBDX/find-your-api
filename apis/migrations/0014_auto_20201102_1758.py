# Generated by Django 3.1.2 on 2020-11-02 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0013_auto_20201102_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postapimodel',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
