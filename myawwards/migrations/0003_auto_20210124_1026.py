# Generated by Django 3.1.5 on 2021-01-24 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='technologies',
            new_name='projects',
        ),
    ]