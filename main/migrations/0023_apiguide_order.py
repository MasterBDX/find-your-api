# Generated by Django 3.1.2 on 2020-12-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_apiguide_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiguide',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
