from django.contrib import admin
from .models import Category, Recipe
from .models import Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Отображаемые поля в списке категорий
    search_fields = ('name',)  # Поля для поиска
    ordering = ('name',)  # Сортировка по имени

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'cooking_time', 'author')  # Отображаемые поля в списке рецептов
    search_fields = ('title', 'author__username')  # Поля для поиска
    list_filter = ('categories',)  # Фильтр по категориям
    ordering = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe', 'quantity', 'created_at')  # Поля для отображения в списке
    search_fields = ('user__username', 'recipe__title')  # Поля для поиска
    list_filter = ('created_at', 'recipe')  # Поля для фильтрации
    ordering = ('-created_at',)  # Сортировка записей