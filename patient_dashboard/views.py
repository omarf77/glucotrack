from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from collections import defaultdict
from patient_blood.models import AddEntry
from homepage.models import PatientProfile


@login_required(login_url='login')
def patient_dashboard(request):
    patient_profile = request.user.patientprofile
    patient = get_object_or_404(PatientProfile, user=request.user)

    last_entry = AddEntry.objects.filter(patient=patient_profile).order_by('-date','-id').first()

    entries = AddEntry.objects.filter(patient=patient).order_by('date')
    chart_data_by_type = defaultdict(list)
    labels_by_type = defaultdict(list)

    for entry in entries:
        reading_type = entry.reading_type  # 'Fasting', 'Random', 'After Meal'
        chart_data_by_type[reading_type].append(entry.blood_sugar)
        labels_by_type[reading_type].append(entry.date.strftime('%b %d'))  

    context = {
        'last_entry': last_entry,
        
        'fasting': chart_data_by_type.get('Fasting', []),
        'labels_fasting': labels_by_type.get('Fasting', []),

        'random': chart_data_by_type.get('Random', []),
        'labels_random': labels_by_type.get('Random', []),

        'after_meal': chart_data_by_type.get('After Meal', []),
        'labels_after_meal': labels_by_type.get('After Meal', []),
        
    }

    return render(request, 'Patient/dashboard.html', context)

def logout_view(request):
    logout(request)  # تحذف الجلسة وتفصل المستخدم
    return redirect('login')  # رجعه على صفحة تسجيل الدخول