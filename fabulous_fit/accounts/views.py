from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def accounts(request):
    return render(request, 'accounts/accounts.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Filter
        username = username.lower()
        # Validation - Check if password match
        if password == password2:
            # Username Validation
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('signup')
            else:
                # Email Validation
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already being used.')
                    return redirect('signup')
                else:
                    # Everything Looks Good
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    # Login After Register
                    # First Method
                    # auth.login(request, user)
                    # messages.success(request, 'You are now registered and can log in.')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in.')
                    return redirect('login')
        else:
            # Register User
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('home')
    else:
        return render(request, 'pages/404_error.html')
