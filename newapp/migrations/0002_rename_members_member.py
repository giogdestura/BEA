# Generated by Django 5.0.6 on 2024-05-14 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]