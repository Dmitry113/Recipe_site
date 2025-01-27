# Generated by Django 5.1.4 on 2025-01-25 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0008_remove_order_email_remove_order_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="delivery_address",
            field=models.CharField(
                default=1, max_length=255, verbose_name="Адрес доставки"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="gift_wrapping",
            field=models.BooleanField(
                default=False, verbose_name="Подарочная упаковка"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="phone_number",
            field=models.CharField(
                default=1, max_length=15, verbose_name="Номер телефона"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="promo_code",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Промокод"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.PositiveIntegerField(verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="order",
            name="recipe",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
            preserve_default=False,
        ),
    ]
