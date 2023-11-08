from django.shortcuts import render
from django.template.defaulttags import register

def home(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)