# Generated by Django 5.0 on 2024-01-12 18:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0003_rename_deadline_todo_dealine"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="deadline",
            new_name="dealine",
        ),
    ]
