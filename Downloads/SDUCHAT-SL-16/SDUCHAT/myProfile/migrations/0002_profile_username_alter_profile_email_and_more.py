# Generated by Django 4.0.1 on 2022-04-01 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
