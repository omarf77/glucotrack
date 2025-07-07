from django.shortcuts import render, redirect
from .forms import PatientSignUpForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PatientSignUpForm()

    return render(request, 'Homepage/signup.html', {'form': form})


