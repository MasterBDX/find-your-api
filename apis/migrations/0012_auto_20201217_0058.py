# Generated by Django 3.1.2 on 2020-12-17 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0011_auto_20201217_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentapimodel',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='commentapimodel',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
