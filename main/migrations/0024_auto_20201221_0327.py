# Generated by Django 3.1.2 on 2020-12-21 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_apiguide_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiguide',
            options={'ordering': ['-order', '-timestamp'], 'verbose_name': 'API Guide', 'verbose_name_plural': 'API Guides'},
        ),
    ]