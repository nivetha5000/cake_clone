from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def birthday(request):
    return render(request, 'birthday.html')

def cart2(request):
    return render(request, 'cart2.html')

def contact(request):
    return render(request, 'contact.html')

def cupcake(request):
    return render(request, 'cupcake.html')

def variety(request):
    return render(request, 'variety.html')

def wedding(request):
    return render(request, 'wedding.html')


# Create your views here.
