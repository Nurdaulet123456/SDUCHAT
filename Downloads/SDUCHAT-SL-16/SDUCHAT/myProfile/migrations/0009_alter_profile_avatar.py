# Generated by Django 4.0.2 on 2022-05-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0008_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='media/img/icons8-account-48.png', upload_to='media/img/'),
        ),
    ]