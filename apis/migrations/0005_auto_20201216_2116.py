# Generated by Django 3.1.2 on 2020-12-16 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20201214_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentapimodel',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='commentapimodel',
            old_name='user_id',
            new_name='user',
        ),
    ]
