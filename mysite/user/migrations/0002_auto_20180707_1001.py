# Generated by Django 2.0 on 2018-07-07 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_type',
        ),
        migrations.DeleteModel(
            name='BlogType',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
