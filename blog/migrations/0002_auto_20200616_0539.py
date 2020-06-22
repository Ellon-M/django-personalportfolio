# Generated by Django 3.0.7 on 2020-06-16 02:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 16, 2, 38, 38, 637116, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_description',
            field=models.TextField(default=datetime.datetime(2020, 6, 16, 2, 39, 13, 367961, tzinfo=utc)),
            preserve_default=False,
        ),
    ]