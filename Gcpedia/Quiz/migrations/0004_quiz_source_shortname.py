# Generated by Django 2.1 on 2018-09-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_auto_20180920_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_source',
            name='shortName',
            field=models.CharField(default='missing short name', max_length=8),
        ),
    ]