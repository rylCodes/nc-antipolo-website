# Generated by Django 4.2.1 on 2023-06-06 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nc_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('expertise', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('Expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='nc_app.expert')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='nc_app.expert')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('Expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='nc_app.expert')),
            ],
        ),
    ]