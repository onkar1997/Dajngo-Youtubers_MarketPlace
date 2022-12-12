from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HireYoutuber


def hire_youtubers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']
        youtuber_id = request.POST['youtuber_id']
        youtuber_name = request.POST['youtuber_name']

        hire_youtubers = HireYoutuber(first_name=first_name, last_name=last_name, email=email, phone=phone, city=city,
                                      state=state, message=message, user_id=user_id, youtuber_id=youtuber_id, youtuber_name=youtuber_name)
        hire_youtubers.save()
        messages.success(request, 'Thanks for reaching out.')
        return redirect('youtubers')
