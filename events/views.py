from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventRegistrationForm
from .models import EventRegistration
from django.contrib.auth.hashers import make_password

def register_event(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)

        if form.is_valid():
            registration = form.save(commit=False)
            registration.password = make_password(form.cleaned_data['password'])
            registration.save()
            messages.success(request, "🎉 Registration successful! Welcome to the event.")
            return redirect('success')
    else:
        form = EventRegistrationForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')