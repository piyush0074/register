from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as save_login
from django.contrib import messages
from django import forms
from .form import NewUserForm
from . import views

# Create your views here.
def home(request):
    return render(request = request,
                  template_name='home.html',
                  context = {"tutorials":Tutorial.objects.all})

def login(request):
	if request.method == "POST":
		form= AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username= form.cleaned_data.get("username")
			password= form.cleaned_data.get("password")
			user= authenticate(username=username,password=password)
			if user is not None:
				save_login(request,user)
				messages.info(request,f"You are now logged in as {{username}}")
				return redirect('/')
			else:
				messages.error(request,"Invalid username or password")
		else:
			messages.error(request,"Invalid username or password")
	form = AuthenticationForm()
	return render(request=request,template_name="login.html",context={"form":form})

def register(request):
	form = NewUserForm(request.POST or None)
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user= form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f"Registered Successfull : {username}")
			save_login(request, user)
			messages.info(request,f"You are now logged in as {username}")
			return redirect('/')
	else:
		for msg in form.error_messages:
			messages.error(request,f"{msg}: {form.error_messages[msg]}")
	
		
	form = NewUserForm
	return render(request,"register.html",context={"form":form})

def logout_user(request):
	logout(request)
	messages.info(request,f"Logout Successfully!!")
	return redirect('/')

