from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import auth 
from note import views

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            #checks if both passwords are same
            try:
                #checks if username exists
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password1)
                auth.login(request, user)
                print('done')
                return redirect('note:home')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
            #checks if username exists
            auth.login(request, user)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error':'user does not exists'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('note:home')
    else:
        return render(request, 'login.html')