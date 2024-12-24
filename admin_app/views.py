from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

 #path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name="Logout"),

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"home.html")

#def login(request):
#    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'u account has been created..')
            return redirect('Login')
        else:
            messages.warning(request,'password mismatching...!')
            return redirect('Register')
    else:
       form=CreateUserForm()
       return render(request,"register.html",{'form':form})

@login_required   
def profile(request):
    return render(request,"profile.html")

def logout_v(request):
    logout(request) 
    return render(request,'logout.html')
