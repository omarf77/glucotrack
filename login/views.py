from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from homepage.models import PatientProfile


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_medical_staff:
                return redirect('medical_staff_dashboard')
            
            try:
                patient_profile = PatientProfile.objects.get(user=user)

                if patient_profile.diabetes_type == "Gestational":
                    return redirect('gestational_dashboard')
                else:
                    return redirect('patient_dashboard')
                
            except PatientProfile.DoesNotExist:
                messages.error(request, "No patient profile found.")    
            
        else:
            messages.error(request, "Email or password is incorrect.")

    return render(request, 'Homepage/login.html')

