# Generated by Django 4.0.1 on 2022-04-22 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_message_subject_message_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 13, 27, 24, 643597)),
        ),
    ]
