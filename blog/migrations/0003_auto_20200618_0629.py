# Generated by Django 3.0.7 on 2020-06-18 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200616_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='main_title',
            new_name='title',
        ),
    ]
