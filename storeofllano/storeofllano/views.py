from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm

# from django.contrib.auth.models import User
from users.models import User

from products.models import Product

def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request,'index.html',{
        # Contexto 
        'title':'store of llano',
        'message':'Listado de productos',
        'products':products
    })

def login_views(request):
    if request.user.is_authenticated:
        return redirect('index')
        
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
        'title':'Login - storeofllano',
    })

def logout_views(request):
    logout(request)
    messages.success(request,'Se cerro correctamente la sesión')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method=='POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')


    return render(request,'users/register.html',{
        'form':form,
        'title':'Registro - storeofllano',
    })

