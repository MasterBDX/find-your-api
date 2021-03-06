# Generated by Django 3.1.2 on 2020-11-16 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suggestion',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
