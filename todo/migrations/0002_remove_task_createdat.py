# Generated by Django 5.1.5 on 2025-01-17 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='createdAt',
        ),
    ]
