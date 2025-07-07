from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def patient_game(request):
 return render(request,'Patient/game.html')