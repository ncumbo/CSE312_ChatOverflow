# Generated by Django 2.2.12 on 2020-04-20 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
