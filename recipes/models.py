from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Состав")
    cooking_time = models.IntegerField(verbose_name="Время приготовления (в минутах)")
    steps = models.TextField(verbose_name="Рецепт салата")
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True, verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    categories = models.ManyToManyField(Category, related_name='recipes', verbose_name="Категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"



