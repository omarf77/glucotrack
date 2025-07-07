from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def medical_prevention_test(request):
 return render(request,'Medical/prevention_test.html' )