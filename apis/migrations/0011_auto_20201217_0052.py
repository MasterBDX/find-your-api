# Generated by Django 3.1.2 on 2020-12-17 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_remove_commentapimodel_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentapimodel',
            old_name='userId',
            new_name='user_id',
        ),
    ]
