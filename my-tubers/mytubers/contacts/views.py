from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

        contacts = Contact(full_name=full_name, email=email, phone=phone,
                           company_name=company_name, subject=subject, message=message)
        contacts.save()
        messages.success(
            request, 'Thanks for contacting. We\'ll get back to you soon')
        return redirect('contact')
    return render(request, 'webpages/contact.html')
