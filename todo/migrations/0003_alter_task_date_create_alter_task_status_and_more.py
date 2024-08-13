# Generated by Django 5.0.7 on 2024-07-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_task_options_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date_create",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(related_name="tasks", to="todo.tag"),
        ),
    ]
