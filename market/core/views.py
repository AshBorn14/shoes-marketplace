from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import SignUpForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request,'core/index.html',{
        'categories':categories, 'items': items,
    })


def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('core:home')
    else:
        form = SignUpForm()
        return render(request,'core/signup.html',{
            'form':form
            })
    return render(request,'core/signup.html',{
            'form':form
            })
        

def logout_user(request):
    logout(request)

    return redirect('core:home')
    
    
