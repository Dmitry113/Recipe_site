from django import forms
from .models import Recipe, Category, Order
from django.forms import ModelChoiceField


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user', 'recipe', 'quantity',
            'delivery_address', 'phone_number',
            'gift_wrapping', 'promo_code'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = self.fields['user'].queryset.filter(is_active=True)



