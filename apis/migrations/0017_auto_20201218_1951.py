# Generated by Django 3.1.2 on 2020-12-18 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0016_auto_20201218_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postapimodel',
            name='published_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
