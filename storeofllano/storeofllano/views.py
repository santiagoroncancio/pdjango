from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm

from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html',{
        # Contexto 
        'title':'store of llano',
        'message':'Listado de productos',
        'products':[
            {'title':'Camisa','price':5,'stock':True}, 
            {'title':'Pantalon','price':7,'stock':True},
            {'title':'Gorra','price':2,'stock':True},
            {'title':'Medias','price':1,'stock':False},
        ]
    })

def login_views(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña no validos')

    return render(request,'users/login.html',{

    })

def logout_views(request):
    logout(request)
    messages.success(request,'Se cerro correctamente la sesión')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method=='POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')


    return render(request,'users/register.html',{
        'form':form
    })

