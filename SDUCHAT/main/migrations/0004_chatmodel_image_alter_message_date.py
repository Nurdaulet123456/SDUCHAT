# Generated by Django 4.0.4 on 2022-05-20 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmodel',
            name='image',
            field=models.ImageField(default='image/account.png', null=True, upload_to='media/image'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 17, 39, 33, 94732)),
        ),
    ]