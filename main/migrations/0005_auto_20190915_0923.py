# Generated by Django 2.2.5 on 2019-09-15 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190914_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 9, 23, 10, 745724, tzinfo=utc), verbose_name='date published'),
        ),
    ]
