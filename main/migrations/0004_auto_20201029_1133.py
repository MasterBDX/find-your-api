# Generated by Django 3.1.2 on 2020-10-29 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_api_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Api',
            new_name='ApiGuide',
        ),
    ]
