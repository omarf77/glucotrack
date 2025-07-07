from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def patient_kidsgame(request):
 return render(request,'Patient/kids2.html')