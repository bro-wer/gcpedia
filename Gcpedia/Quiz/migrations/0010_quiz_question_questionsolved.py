# Generated by Django 2.1 on 2018-09-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0009_auto_20180920_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_question',
            name='questionSolved',
            field=models.BooleanField(default=False),
        ),
    ]
