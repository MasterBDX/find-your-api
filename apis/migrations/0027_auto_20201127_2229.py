# Generated by Django 3.1.2 on 2020-11-27 22:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0026_auto_20201125_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postapimodel',
            name='published_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]