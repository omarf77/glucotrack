# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BloodSugarReadingForm
from homepage.models import PatientProfile
from .models import AddEntry 

@login_required(login_url='login')
def patient_blood(request):
    if request.method == 'POST':
        form = BloodSugarReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.patient = PatientProfile.objects.get(user=request.user)
            reading.save()
            return redirect('patient_blood')
    else:
        form = BloodSugarReadingForm()

    # جلب السجلات الخاصة بالمستخدم الحالي
    patient = PatientProfile.objects.get(user=request.user)
    history = AddEntry.objects.filter(patient=patient).order_by('-date')[:5]

    return render(request, 'Patient/add_blood_entry.html', {
        'form': form,
        'history': history
    })