# Generated by Django 4.2.1 on 2023-06-09 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nc_app', '0008_alter_detail_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='Expert',
            new_name='mentor',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='Expert',
            new_name='mentor',
        ),
    ]