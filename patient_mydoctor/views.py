from django.shortcuts import render,redirect

from django.db.models import Count
from homepage.models import MedicalStaffProfile
from medical_staff_patients.models import ChatMessage
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def assign_doctor(request):
    patient = request.user.patientprofile
    doctor = MedicalStaffProfile.objects.annotate(num_patients=Count('patients')).order_by('num_patients').first()

    if doctor:
        patient.doctor = doctor
        patient.is_approved = False  # لسه ما وافق عليه الدكتور
        patient.save()
        messages.info(request, "Waiting for doctor's approval.")
    return redirect('patient_mydoctor')  # تأكد إن اسم الـ url هذا مضبوط


@login_required(login_url='login')
def patient_mydoctor(request):
    patient = request.user.patientprofile
    doctor = patient.doctor if patient.is_approved else None

    chat_messages = []
    if doctor:
        chat_messages = ChatMessage.objects.filter(
            sender__in=[request.user, doctor.user],
            receiver__in=[request.user, doctor.user]
        )

    context = {
        'patient': patient,
        'doctor': doctor,
        'messages': chat_messages,  # ✅ أضفنا الرسائل هنا
    }
    return render(request, 'Patient/mydoctor.html', context)


    