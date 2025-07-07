from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from patient_blood.models import AddEntry
from django.db.models import Max
from homepage.models import PatientProfile,CustomUser
from .models import ChatMessage
from django.contrib import messages

@login_required(login_url='login')
def medical_staff_patients(request):
    doctor = request.user.medicalstaffprofile

    # المرضى المرتبطين مع هذا الدكتور فقط
    patients = PatientProfile.objects.filter(doctor=doctor).select_related('user')

    approved_patients = patients.filter(is_approved=True)

    pending_patients = patients.filter(is_approved=False)
    # آخر قراءة لكل مريض
    latest_dates = AddEntry.objects.filter(patient__in=patients)\
        .values('patient_id')\
        .annotate(latest_date=Max('date'))

    # نجلب القراءة المرتبطة مع كل مريض حسب التاريخ الأحدث
    latest_readings = {
    item['patient_id']: AddEntry.objects
        .filter(patient_id=item['patient_id'], date=item['latest_date'])
        .order_by('id')  # أو بأي ترتيب بدك إياه
        .first()
    for item in latest_dates
}

    return render(request, 'Medical/patients.html', {
        'patients': patients,
        'latest_readings': latest_readings,
        'pending_patients': pending_patients,
        'approved_patients': approved_patients

    })

@login_required(login_url='login')
def approve_patient(request, patient_id):
    patient = get_object_or_404(PatientProfile, id=patient_id, doctor=request.user.medicalstaffprofile)
    patient.is_approved = True
    patient.save()
    return redirect('medical_staff_patients')

@login_required(login_url='login')
def reject_patient(request, patient_id):
    patient = get_object_or_404(PatientProfile, id=patient_id)

    if patient.doctor == request.user.medicalstaffprofile and not patient.is_approved:
        patient.doctor = None  # فك الربط
        patient.save()
    
    return redirect('medical_staff_patients')


@login_required(login_url='login')
def patient_detail(request, pk):
    patient = get_object_or_404(PatientProfile, pk=pk)
    entries = AddEntry.objects.filter(patient=patient).order_by('-date')

    return render(request, 'Medical/patient_detail.html', {
        'patient': patient,
        'entries': entries
    })

@login_required(login_url='login')
def delete_patient(request, patient_id):
    patient = get_object_or_404(PatientProfile, id=patient_id)

    if patient.doctor == request.user.medicalstaffprofile:
        patient.doctor = None  # فك الربط
        patient.save()

        ChatMessage.objects.filter(
            sender__in=[request.user, patient.user],
            receiver__in=[request.user, patient.user]
        ).delete()
    
    return redirect('medical_staff_patients')


@require_POST
@login_required(login_url='login')
def bulk_patient_action(request):
    doctor = request.user.medicalstaffprofile
    selected_ids = request.POST.getlist('selected_patients')
    action = request.POST.get('action')

    if not selected_ids:
        messages.warning(request, "No patients selected.")
        return redirect('medical_staff_patients')

    patients = PatientProfile.objects.filter(id__in=selected_ids, doctor=doctor, is_approved=False)

    if action == 'approve':
        patients.update(is_approved=True)
        messages.success(request, f"{patients.count()} patient(s) approved.")
    elif action == 'reject':
        for patient in patients:
            patient.doctor = None
            patient.save()
        messages.success(request, f"{patients.count()} patient(s) rejected.")
    else:
        messages.error(request, "Invalid action.")

    return redirect('medical_staff_patients')



@login_required(login_url='login')
def chat(request, user_id):
    target_user = CustomUser.objects.get(id=user_id)
    messages = ChatMessage.objects.filter(
        sender__in=[request.user, target_user],
        receiver__in=[request.user, target_user]
    ).order_by('-timestamp')

    if request.method == 'POST':
        msg = request.POST.get('message')
        ChatMessage.objects.create(sender=request.user, receiver=target_user, message=msg)
        return redirect('chat', user_id=user_id)

    return render(request, 'Medical/chat.html', {'target_user': target_user, 'messages': messages})

@login_required(login_url='login')
def mark_reading_seen(request, reading_id):
    reading = get_object_or_404(AddEntry, id=reading_id)
    if reading.patient.doctor.user == request.user:
        reading.seen_by_doctor = True
        reading.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='login')
def mark_all_readings_seen(request, patient_id):
    entries = AddEntry.objects.filter(patient_id=patient_id, patient__doctor__user=request.user)
    entries.update(seen_by_doctor=True)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def get_messages(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    messages = ChatMessage.objects.filter(
        sender__in=[request.user, target_user],
        receiver__in=[request.user, target_user]
    ).order_by('timestamp')[:50]

    message_data = [
        {
            'sender': msg.sender.username,
            'message': msg.message,
            'timestamp': msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for msg in messages
    ]
    return JsonResponse({'messages': message_data})