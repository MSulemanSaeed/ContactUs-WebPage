from django.shortcuts import render
from .models import Contact
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def about_view(request):
    return render(request, 'about.html')

def products_view(request):
    return render(request, 'products.html')