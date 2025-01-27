import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RecipeForm, OrderForm
from .models import Recipe, Order
from django.contrib import messages

# Настройка логирования
log = logging.getLogger(__name__)

# Главная страница
def home(request):
    log.info("Главная страница загружена")
    recipes = Recipe.objects.order_by('?')[:5]  # Выбираем 5 случайных рецептов
    return render(request, 'recipes/home.html', {'recipes': recipes})

# Добавление или редактирование рецепта
def recipe_form(request, recipe_id=None):  # Используем recipe_id для идентификации рецепта
    if not request.user.is_authenticated:
        log.warning(f"Попытка неавторизованного доступа к редактированию рецепта. Пользователь: {request.user}")
        return redirect('login')

    recipe = None
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        log.info(f"Редактирование рецепта: {recipe.title} (ID: {recipe_id})")
    else:
        log.info("Добавление нового рецепта")

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            log.info(f"Рецепт '{recipe.title}' успешно сохранён пользователем {request.user}")
            return redirect('home')
        else:
            log.error(f"Ошибка при сохранении рецепта. Данные формы: {form.errors}")
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe_form.html', {'form': form})

# Вход
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            log.info(f"Пользователь {username} успешно вошёл в систему")
            return redirect('home')
        else:
            log.warning(f"Неудачная попытка входа для пользователя: {username}")
    return render(request, 'recipes/login.html')

# Регистрация
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            log.info(f"Новый пользователь зарегистрирован: {user.username}")
            return redirect('login')
        else:
            log.error(f"Ошибка регистрации. Данные формы: {form.errors}")
    else:
        form = UserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})

# Выход
def logout_view(request):
    log.info(f"Пользователь {request.user} вышел из системы")
    logout(request)
    return redirect('home')

# Детальная страница рецепта
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    log.info(f"Загружена страница рецепта: {recipe.title} (ID: {pk})")
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Создание нового заказа
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем заказ
            return redirect('order_success')  # Перенаправление на страницу успеха
    else:
        form = OrderForm()

    return render(request, 'recipes/create_order.html', {'form': form})

# Успех заказа
def order_success(request):
    last_order = Order.objects.last()  # Получаем последний заказ
    return render(request, 'recipes/order_success.html', {'order': last_order})

# Список всех заказов
def orders_list(request):
    orders = Order.objects.all()  # Получаем все заказы
    return render(request, 'recipes/orders_list.html', {'orders': orders})

# Представление для удаления заказа
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('orders_list')  # Перенаправляем на список заказов после удаления

def contact_view(request):
    if request.method == 'POST':
        # Обработать форму
        pass
    return render(request, 'contacts/contact.html')
