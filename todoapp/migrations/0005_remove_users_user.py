# Generated by Django 3.2.6 on 2021-09-21 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20210921_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
    ]