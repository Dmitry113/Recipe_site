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
    path('create_order/', views.create_order, name='create_order'),  # Страница создания заказа
    path('order_success/', views.order_success, name='order_success'),  # Страница успеха
    path('orders/', views.orders_list, name='orders_list'),  # Страница списка заказов
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),  # Удаление заказа
    path('', views.contact_view, name='contact'),  # Это маршрут для страницы контактов
]
