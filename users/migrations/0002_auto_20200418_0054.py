# Generated by Django 3.0.5 on 2020-04-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_bio',
            field=models.CharField(default='Change current Bio', max_length=300),
        ),
    ]
