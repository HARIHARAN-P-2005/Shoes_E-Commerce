from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate

def index(request):
    return render(request, 'index.html')

def Men(request):
    return render(request, 'Men.html')

def women(request):
    return render(request, 'women.html')

def About(request):
    return render(request, 'About.html')

def view(request):
    return render(request, 'view.html')

def Views(request):
    return render(request, 'Views.html')

def Mencollection(request):
    return render(request, 'Mencollection.html')

def Womencollection(request):
    return render(request, 'Womencollection.html')

def Sportscollection(request):
    return render(request, 'Sportscollection.html')

def Formalcollection(request):
    return render(request, 'Formalcollection.html')

def purchase(request):
    return render(request, 'purchase.html')

def Purchasenow(request):
    return render(request, 'Purchasenow.html')

def Now(request):
    return render(request, 'Now.html')

def add(request):
    return render(request, 'add.html')

def to(request):
    return render(request, 'to.html')

def cart(request):
    return render(request, 'cart.html')
def shoe(request):
    return render(request, 'shoe.html')

def formal(request):
    return render(request, 'formal.html')

def loginPage(request):
    if(request=='POST'):
        name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=name,password=password)
        if(user is not None):
            return HttpResponse("Login Fail")
        else:
            return render(request, 'index.html')
    return render(request,'login.html')