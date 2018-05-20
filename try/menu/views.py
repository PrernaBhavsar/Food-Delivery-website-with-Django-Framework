from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from .forms import Signup_form, Login_form, menu_form
from .models import Signup
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.contrib import messages
# hashed_pwd = make_password("plain_text")
# check_password("plain_text",hashed_pwd)  # returns True
# Create your views here.

plan={1:'Premium',2:'Pro',3:'Starter'}

def signup(request,no):
    if(request.method == 'GET'):
        return redirect('/confirm_signup'+no+'/')

def confirm_signup(request, no):
    print("Hello")
    if request.method == "POST":
        form_var = Signup_form(data=request.POST)
        print(form_var.is_valid(), form_var.errors, type(form_var.errors))
        print(no)
        if form_var.is_valid():
            print('Im here')
            match=Signup.objects.filter(email=form_var.cleaned_data['email'])
            if match:
                return render(request, 'menu/indexsameemail.html')
            model_obj = form_var.save()
            model_obj.password = make_password(form_var.cleaned_data['password'])
            model_obj.plan = plan[int(no)]
            model_obj.save()
            print(model_obj.password)
            return render(request,'menu/indexregister.html')
        else:
            return render(request, 'menu/indexerror.html')
    else:
        url="confirm_signup"+no+"/"
        print(url)
        return render(request, "menu/indexsignup.html",{'url': url})


def login(request):
    if request.method == "POST":
        form_obj = Login_form(data=request.POST)
        print(form_obj.is_valid(), form_obj.errors, type(form_obj.errors))
        if form_obj.is_valid():
            email_id=form_obj.cleaned_data['email']
            password= form_obj.cleaned_data['password']
            model_obj = Signup.objects.all()
            found = model_obj.filter(email=email_id)
            print(found)
            if not found:
                return render(request, 'menu/loginerror.html')
            print(password)
            print(found[0].password)
            my_plan = found[0].plan
            print(my_plan)
            if(my_plan == "Premium"):
                found[0].total = 13.30
            elif(my_plan == "Pro"):
                found[0].total = 14.90
            elif(my_plan == "Starter"):
                found[0].total = 19.0
            found[0].save()
            print("\n\n\n")
            print(found[0].total)
            if check_password(password,found[0].password):
                return render(request, 'menu/details.html', {'found':found[0]})
            else:
                return render(request, 'menu/incorrectpass.html')
        else:
            return render(request, 'menu/indexerror.html')
    else:
        form_obj = Login_form()
    return render(request, "menu/indexsignup.html", {'form': form_obj})


def index(request, pk):
    found = Signup.objects.get(id=pk)
    print(found)
    if request.method=="POST":
        form_obj = menu_form(data=request.POST)
        print("\n\nPOST______")
        print(form_obj.is_valid(), form_obj.errors, type(form_obj.errors))
        if form_obj.is_valid():
            print("\n\n\n")
            print("Valid")
            found.order = form_obj.cleaned_data['order']
            found.save()
        return render(request, 'menu/confirmorder.html',{'found':found})
    return render(request,'menu/indexmenu.html',{'found':found})




