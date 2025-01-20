from django.contrib import admin
from .models import Recipe, Category

# Настроим отображение модели Recipe в админке
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time', 'image')  # Здесь указываем, какие поля будут отображаться в списке
    search_fields = ('title', 'author__username')  # По каким полям будем искать
    list_filter = ('author', 'categories')  # Фильтрация по автору и категориям

    # Поля на форме редактирования
    fields = ('title', 'description', 'cooking_time', 'steps', 'image', 'author', 'categories')

# Зарегистрируем модель Recipe и Category с настройками админки
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
