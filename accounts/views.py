from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import Account
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email= form.cleaned_data['email']
            phone_number= form.cleaned_data['phone_number']
            password= form.cleaned_data['password']
            username = email.split("@")[0]

            user= Account.objects.create_user(email=email,first_name=first_name,last_name=last_name,
            username=username,password=password)
            user.phone_number=phone_number
            user.save()
            messages.success(request, 'Your profile was created.')
            return redirect ('register')
    else:   
        form = RegisterForm()
    context ={
        'form': form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)

            redirect('home')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
        
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,'accounts/logout.html')