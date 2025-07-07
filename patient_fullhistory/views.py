from django.shortcuts import render
from patient_blood.models import AddEntry
from homepage.models import PatientProfile
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def patient_full_history(request):
    patient = PatientProfile.objects.get(user=request.user)
    all_entries = AddEntry.objects.filter(patient=patient).order_by('-date','-id')
    return render(request, 'Patient/fullhistory.html', {'entries': all_entries})



@login_required(login_url='login')
def delete_entry(request, entry_id):
    entry = get_object_or_404(AddEntry, id=entry_id, patient=request.user.patientprofile)
    entry.delete()
    return redirect('patient_fullhistory')  