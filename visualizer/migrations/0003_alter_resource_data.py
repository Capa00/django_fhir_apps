# Generated by Django 4.1.5 on 2023-01-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visualizer", "0002_alter_resource_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="data",
            field=models.TextField(blank=True, editable=False, verbose_name="Data"),
        ),
    ]
