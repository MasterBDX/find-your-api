# Generated by Django 3.1.2 on 2020-10-31 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20201031_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userapimodel',
            name='email',
        ),
    ]
