from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RecipeForm
from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Главная страница
def home(request):
    recipes = Recipe.objects.all()  # Получаем все рецепты из базы данных
    return render(request, 'recipes/home.html', {'recipes': recipes})


# Добавление рецепта
# Добавление или редактирование рецепта
def recipe_form(request, recipe_id=None):  # Используем recipe_id для идентификации рецепта
    if not request.user.is_authenticated:
        return redirect('login')

    recipe = None
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
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
            return redirect('home')
    return render(request, 'recipes/login.html')

# Регистрация
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})

# Выход
def logout_view(request):
    logout(request)
    return redirect('home')

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
