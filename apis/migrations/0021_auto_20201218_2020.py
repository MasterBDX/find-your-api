# Generated by Django 3.1.2 on 2020-12-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0020_auto_20201218_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentapimodel',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postapimodel',
            name='published_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
