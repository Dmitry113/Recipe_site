from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contacts/contact.html', {'form': form})