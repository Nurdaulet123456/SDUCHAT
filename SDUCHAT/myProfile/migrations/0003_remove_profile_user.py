# Generated by Django 4.0.1 on 2022-04-01 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0002_profile_username_alter_profile_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
