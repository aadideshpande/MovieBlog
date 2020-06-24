from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('home')
        #else:
            #messages.info(request, f'Enter the information according to the instructions')
            #return redirect('register')   
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})