from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model

from accounts.models import Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomProfileChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('post:index')

    if request.method=="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect ('posts:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('post:index')

    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        form2=CustomProfileChangeForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            profile=form2.save(commit=False)
            profile.user=user
            profile.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form=CustomUserCreationForm()
        form2=CustomProfileChangeForm()
    context={
        'form':form,
        'form2':form2,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            request.user.delete()
            return redirect('posts:index')
        else:
            return render(request, 'accounts/delete.html')
    else:
        return redirect('accounts:login')

def update(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('posts:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form':form,
            }
        return render(request, 'accounts/update.html',context)
    else:
        return redirect('accounts:login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('posts:index')
        else:
            form = PasswordChangeForm(request.user)
        context ={
            'form':form,
        }
        return render(request, 'accounts/password.html', context)
    else:
        return redirect('accounts:login')


def profile(request,username):
    User = get_user_model()
    person = get_object_or_404(User, username = username)
    profile = person.profile_set.get(user_id=person.pk)
    posts = person.posts.all()
    context = {
        'person': person,
        'profile' : profile,
        'posts' : posts,
    }
    return render(request, 'accounts/profile.html', context)

def profile_update(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        if request.method=="POST":
            form = CustomProfileChangeForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile', request.user.username)
        else:
            form = CustomProfileChangeForm(instance=profile)
        context = {
            'form':form,
        }
        return render(request,'accounts/profile_update.html', context)

    else:
        return redirect('accounts:login')
