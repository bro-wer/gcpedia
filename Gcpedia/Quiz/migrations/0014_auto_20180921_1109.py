# Generated by Django 2.1 on 2018-09-21 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0013_auto_20180920_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_answer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 11, 9, 21, 291570)),
        ),
        migrations.AddField(
            model_name='quiz_answer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 11, 9, 21, 291570)),
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 11, 9, 21, 290571)),
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 21, 11, 9, 21, 290571)),
        ),
    ]
