# Generated by Django 3.1.2 on 2020-11-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0020_auto_20201103_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentapimodel',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='apis.postapimodel', verbose_name='posts'),
        ),
    ]
