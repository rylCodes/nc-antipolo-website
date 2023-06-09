# Generated by Django 4.2.1 on 2023-06-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nc_app', '0019_mentorbiography_mentoreducation_mentorexperience_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MsmeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AlterField(
            model_name='clientfeedback',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]
