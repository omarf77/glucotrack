from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def patient_prevention_test(request):
 return render(request,'Patient/prevention_test.html' )