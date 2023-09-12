from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt



from user.forms import RegisterForm, LoginForm
from core.models import ProductCategory
from user.models import MyUser

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = RegisterForm()


    context = {
        'title' : 'Register',
        'form' : form,
        'departments' : ProductCategory.objects.all()
    }
    
    return render(request, 'register.html', context=context)


def succes(request):
    context = {
        'title' : "You've registered succesfully"
    }

    return render(request, 'succes.html', context=context)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = MyUser.objects.get(username=username)
            if user is None:
                print('Redirected')
                return redirect('login')
            else:
                if user.password == password:
                    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('home')
                else:
                    print('redirected')
                    return redirect('login')
        else:
            print('form errors', form.errors)
    else:
        form = LoginForm()

    context = {
        'title' : 'Login',
        'form' : form
    }
    
    return render(request, 'login.html', context=context)

def logout(request):
    auth_logout(request)
    return redirect('home')