# Generated by Django 4.2.1 on 2023-06-10 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nc_app', '0012_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ClientFeedback',
        ),
    ]