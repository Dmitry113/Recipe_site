# Generated by Django 5.1.4 on 2025-01-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_recipe_options_alter_recipe_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(verbose_name="Состав"),
        ),
    ]
