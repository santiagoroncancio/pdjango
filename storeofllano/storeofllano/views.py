from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

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
    }
)

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


