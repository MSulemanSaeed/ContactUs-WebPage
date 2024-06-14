from .models import Contact
from django.shortcuts import render, redirect
from .forms import ContactForm

def home_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#home') 
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
