# Generated by Django 4.2.1 on 2023-06-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nc_app', '0007_alter_expert_id_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='description',
            field=models.TextField(),
        ),
    ]