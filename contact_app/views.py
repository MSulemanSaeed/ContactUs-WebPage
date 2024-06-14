# from .models import Contact
# from django.shortcuts import render, redirect
# from .forms import ContactForm

# def home_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/#home') 
#         else:
#             return render(request, 'home.html', {'form': form})
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def home_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email to admin
            subject = 'New Contact Form Submission'
            message = f"""
            Name: {contact.name}
            Phone: {contact.phone}
            Email: {contact.email}
            Status: {contact.status}
            Message: {contact.message_field}
            """
            admin_email = settings.ADMIN_EMAIL
            send_mail(subject, message, settings.EMAIL_HOST_USER, [admin_email])

            return redirect('/#home') 
        else:
            return redirect('/#contact')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
