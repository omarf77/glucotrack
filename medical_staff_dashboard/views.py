from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from homepage.models import MedicalStaffProfile, PatientProfile
from medical_staff_blogs.models import BlogPost
from patient_blood.models import AddEntry
from django.db.models import Q
from collections import Counter


@login_required(login_url='login')
def staff_dashboard(request):

    doctor_profile = get_object_or_404(MedicalStaffProfile, user=request.user)

    # المرضى المرتبطين بهذا الطبيب
    patients = PatientProfile.objects.filter(doctor=doctor_profile)
    
    #  new reading
    new_readings_count = AddEntry.objects.filter(patient__doctor=doctor_profile,seen_by_doctor=False).count()

    # تدوينات الدكتور
    blog_posts_count = BlogPost.objects.filter(doctor=doctor_profile).count()

    # القراءات الخطره لمرضاه
    alerts_count = AddEntry.objects.filter(patient__doctor=doctor_profile).filter(Q(blood_sugar__gt=180) | Q(blood_sugar__lt=70)).count()

    # عدد الملاحظات المكتوبة
    notes_count = AddEntry.objects.filter(Q(patient__doctor=doctor_profile),Q(note__isnull=False) & ~Q(note="")).count()

    # حساب عدد كل نوع سكري باستخدام Counter
    diabetes_counts = Counter(patients.values_list('diabetes_type', flat=True))

    # تحويلها لقاموس من نوع dict
    chart_data = {
        "Type 1": diabetes_counts.get("Type 1", 0),
        "Type 2": diabetes_counts.get("Type 2", 0),
        "Gestational": diabetes_counts.get("Gestational", 0)
    }

    age_groups = {
    '0-18': 0,
    '19-30': 0,
    '31-45': 0,
    '46-60': 0,
    '60+': 0
    }
    for patient in patients:
        age = patient.age
        if age <= 18:
            age_groups['0-18'] += 1
        elif age <= 30:
            age_groups['19-30'] += 1
        elif age <= 45:
            age_groups['31-45'] += 1
        elif age <= 60:
            age_groups['46-60'] += 1
        else:
            age_groups['60+'] += 1

    context = {
        'total_patients': patients.count(),
        'new_readings_count': new_readings_count,
        'blog_posts_count': blog_posts_count,
        'alerts_count': alerts_count,
        'notes_count': notes_count,
        'chart_data': chart_data,
        'age_groups': age_groups,
    }
    return render(request, 'Medical/dashboard.html', context)
         
