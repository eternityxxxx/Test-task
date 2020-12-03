from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserSignupForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)

        return redirect('/')

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)

    return redirect('/')


def signup_view(request):
    form = UserSignupForm(request.POST or None)

    if form.is_valid():
        password = form.cleaned_data.get('password')

        user = form.save(commit=False)
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        return redirect('/')

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)
