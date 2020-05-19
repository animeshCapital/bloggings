from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegisterForm, ProfileForm, UserProfileForm, LoginForm
from blog.models import Post
from .models import UserProfile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from ecom import settings

def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        # paginator = Paginator(posts, 2)
        # try:
        #     posts = paginator.page(page)
        # except PageNotAnInteger:
        #     posts = paginator.page(1)
        # except EmptyPage:
        #     posts = paginator.page(paginator.num_pages)
        # print(posts)
        context = {
            'posts' : posts
        }
        return render(request, 'home.html', context)
    else:
         return redirect('login')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = request.POST.get('email')
            print(email)
            subject = "Registration successfully"
            msg = " Email :-" + email + ",      Password :-" + request.POST.get('password1')
            to = email
            test = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            print(test)
            messages.success(request, 'Registration successfully!')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})     
    else:    
        context = {'form' : form}
        return render(request, 'register.html', context)

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            print('error')    
    context = {
        'form': form
        
    }
    return render(request, 'login.html', context)

def profile_edit(request, *args, **kwargs):
    user = request.user
    p_form = ProfileForm(request.POST or None, instance=user)
    u_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user.userprofile)
    if request.method == 'POST':
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Profile Update successfully!')
            return redirect('home')

    context = {
        'p_form': p_form,
        'u_form': u_form,
        'object': user
    }
    return render(request, 'profile/edit.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile/change_password.html', {
        'form': form
    })

def logout_page(request):
    logout(request)
    return redirect('login')