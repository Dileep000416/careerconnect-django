from django.shortcuts import render, redirect
from django.contrib.auth import (
    login,
    logout,
    authenticate
)
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .forms import (
    RegisterForm,
    ProfileUpdateForm
)
from .models import UserProfile


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = RegisterForm()

    context = {
        'form': form
    }

    return render(
        request,
        'accounts/register.html',
        context
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

    return render(
        request,
        'accounts/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('home')


@login_required
def profile_view(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    context = {
        'profile': profile
    }

    return render(
        request,
        'accounts/profile.html',
        context
    )


@login_required
def edit_profile_view(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect('profile')

    else:

        form = ProfileUpdateForm(
            instance=profile
        )

    context = {
        'form': form,
        'profile': profile
    }

    return render(
        request,
        'accounts/edit_profile.html',
        context
    )