from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('recipe/new/', views.recipe_form, name='new_recipe'),  # Добавить рецепт
    path('recipe/<int:recipe_id>/edit/', views.recipe_form, name='edit_recipe'),  # Маршрут для редактирования рецепта
    path('login/', views.login_view, name='login'),  # Страница входа
    path('signup/', views.signup_view, name='signup'),  # Страница регистрации
    path('logout/', views.logout_view, name='logout'),  # Выход
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # Детали рецепта
]
