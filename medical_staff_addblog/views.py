from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def medical_staff_addblog(request):
 return render(request,'Medical/add_blog.html' )
