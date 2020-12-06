# Generated by Django 3.1.2 on 2020-12-04 17:56

import apis.global_utils
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserApiModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=255)),
                ('birthday', models.DateField()),
                ('birth_place', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users Api',
            },
        ),
        migrations.CreateModel(
            name='PostApiModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=apis.global_utils.get_thumnail_name)),
                ('published_at', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.userapimodel')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts Api',
            },
        ),
        migrations.CreateModel(
            name='CommentApiModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='apis.postapimodel', verbose_name='posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='apis.userapimodel')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments Api',
            },
        ),
    ]
