from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from youtubers.models import Youtuber
from hireyoutubers.models import HireYoutuber


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if len(password) > 6:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'Username already exists!')
                    return redirect('signup')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.warning(request, 'Email already exists!')
                        return redirect('signup')
                    else:
                        user = User.objects.create_user(
                            first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                        user.save()
                        messages.success(
                            request, 'Account created successfully.')
                        return redirect('signin')
            else:
                messages.warning(
                    request, 'Password should be atleast 7 characters long!')
                return redirect('signup')
        else:
            messages.warning(request, 'Password do not match!')
            return redirect('signup')

    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are signed in successfully.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials!')
            return redirect('signin')

    return render(request, 'accounts/signin.html')


@login_required(login_url='signin')
def dashboard(request):
    youtubers = Youtuber.objects.all()
    hired_youtubers = HireYoutuber.objects.all()

    data = {
        'youtubers': youtubers,
        'hired_youtubers': hired_youtubers
    }
    return render(request, 'accounts/dashboard.html', data)


def signout(request):
    logout(request)
    messages.success(request, 'You are signed out successfully')
    return redirect('home')
