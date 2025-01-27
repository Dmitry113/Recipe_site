from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите ваш email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите ваш номер телефона'}),
            'message': forms.Textarea(attrs={'placeholder': 'Введите сообщение', 'rows': 5}),
        }