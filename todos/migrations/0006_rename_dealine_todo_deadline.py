# Generated by Django 5.0.1 on 2024-01-13 14:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0005_alter_todo_dealine"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="dealine",
            new_name="deadline",
        ),
    ]
