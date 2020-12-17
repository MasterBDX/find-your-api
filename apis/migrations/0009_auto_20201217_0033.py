# Generated by Django 3.1.2 on 2020-12-17 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20201216_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentapimodel',
            name='email',
            field=models.EmailField(default='email@mail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='commentapimodel',
            name='userId',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='commentapimodel',
            name='username',
            field=models.CharField(default='username', max_length=255),
        ),
    ]
