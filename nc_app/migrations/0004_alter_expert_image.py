# Generated by Django 4.2.1 on 2023-06-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nc_app', '0003_expert_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/mentors'),
        ),
    ]
