# Generated by Django 4.0.2 on 2022-05-22 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_message_date_starred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 13, 10, 36, 425717)),
        ),
    ]