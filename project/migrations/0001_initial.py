# Generated by Django 4.0 on 2023-08-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a priority name', max_length=255, verbose_name='Priority')),
                ('description', models.TextField(help_text='Must contain only 3000 characters', max_length=3000, verbose_name='Priority description')),
                ('is_active', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a project name', max_length=255, verbose_name='Project title')),
                ('description', models.TextField(help_text='Must contain only 3000 characters', max_length=3000, verbose_name='Project description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a status name', max_length=255, verbose_name='Status title')),
                ('description', models.TextField(help_text='Must contain only 3000 characters', max_length=3000, verbose_name='Status description')),
                ('is_active', models.BooleanField(null=True)),
            ],
        ),
    ]
