# Generated by Django 3.1.2 on 2020-12-16 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_remove_commentapimodel_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentapimodel',
            old_name='postId',
            new_name='post_id',
        ),
    ]
