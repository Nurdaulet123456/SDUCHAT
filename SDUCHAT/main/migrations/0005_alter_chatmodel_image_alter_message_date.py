# Generated by Django 4.0.4 on 2022-05-20 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_chatmodel_image_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='image',
            field=models.ImageField(default='img/account.png', null=True, upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 17, 42, 32, 853964)),
        ),
    ]
