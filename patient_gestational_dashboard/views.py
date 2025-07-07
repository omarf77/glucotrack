from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from patient_blood.models import AddEntry
from datetime import timedelta
from django.db.models import Avg
from collections import defaultdict

# Create your views here.


@login_required(login_url='login')
def gestational_dashboard(request):
    patient = request.user.patientprofile
    today = timezone.now().date()
    past_30_days = today - timedelta(days=30)
    week_ago = today - timedelta(days=7)
 

    readings = AddEntry.objects.filter(patient=patient, date__gte=past_30_days)

    # حساب المعدل
    avg_glucose = readings.aggregate(avg=Avg('blood_sugar'))['avg'] or 0

    # آخر قراءة
    last_reading = readings.order_by('-date').first()
    last_glucose = last_reading.blood_sugar if last_reading else None

    # حالة التنبيه (alert)
    if last_glucose is not None:
        if last_glucose > 180:
            alert = ("High", "danger")
        elif last_glucose < 70:
            alert = ("Low", "warning")
        else:
            alert = ("Normal", "success")
    else:
        alert = ("N/A", "secondary")

    # overall health
    if avg_glucose > 180:
        overall_status = ("Unstable", "danger")
    elif avg_glucose < 70:
        overall_status = ("Low", "warning")
    else:
        overall_status = ("Stable", "primary")

   

    entries = AddEntry.objects.filter(patient=patient).order_by('date')
    chart_data =[]
    labels =[]
    
   

    for entry in entries:
        
        chart_data.append(entry.blood_sugar)
        labels.append(entry.date.strftime('%b %d'))  


    context = {
        'avg_glucose': round(avg_glucose, 1),
        'last_glucose': last_glucose,
        'alert_status': alert,
        'overall_status': overall_status,
        'allentry': chart_data,
        'labels_allentry': labels,
    }

    
    return render(request, 'Patient/gestational_dashboard.html',context)

