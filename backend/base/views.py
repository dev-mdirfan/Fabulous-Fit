from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Category

def home(request):
    return render(request, 'base/home.html')

def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password is incorrect')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    page = 'register'
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred during registration')
    
    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)

def all_categories(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', default=1))
        current_category = Category.objects.get(pk=category_id)

        children = current_category.get_children()
        ancestors = current_category.get_ancestors()
        products = current_category.products.all()

        context = {
            'categories': children,
            'current_category': current_category,
            'ancestors': ancestors,
            'products': products,
        }
    return render(request, 'base/all_categories.html', context)