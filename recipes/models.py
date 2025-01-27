from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db import models
timezone.now()



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Состав")
    cooking_time = models.IntegerField(verbose_name="Время приготовления (в минутах)")
    steps = models.TextField(verbose_name="Рецепт")
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True, verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    categories = models.ManyToManyField(Category, related_name='recipes', verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Заказчик"
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        verbose_name="Название рецепта"
    )
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    delivery_address = models.CharField(
        max_length=255,
        verbose_name="Адрес доставки"
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона"
    )
    gift_wrapping = models.BooleanField(
        default=False,
        verbose_name="Подарочная упаковка"
    )
    promo_code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Промокод"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ {self.id} от {self.user}"






