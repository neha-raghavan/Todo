# Generated by Django 3.2.6 on 2021-09-21 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_auto_20210921_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user',
            new_name='username',
        ),
    ]
