# Generated by Django 3.1.2 on 2020-11-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201118_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='name',
            field=models.CharField(default='Find Your Api', max_length=255),
            preserve_default=False,
        ),
    ]