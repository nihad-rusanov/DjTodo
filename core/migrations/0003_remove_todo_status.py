# Generated by Django 4.2.7 on 2023-11-18 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
    ]
