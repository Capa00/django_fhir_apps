# Generated by Django 4.1.5 on 2023-01-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visualizer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="name",
            field=models.CharField(editable=False, max_length=255, verbose_name="Name"),
        ),
    ]