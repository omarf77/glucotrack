"""
URL configuration for glucotrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('login/',include('login.urls')),
    path('signup/',include('signup.urls')),
    ######################################################### Medical staff
    path('medical_staff_addblog/',include('medical_staff_addblog.urls')),
    path('medical_staff_blogs/',include('medical_staff_blogs.urls')),
    path('medical_staff_dashboard/',include('medical_staff_dashboard.urls')),
    path('medical_staff_patients/',include('medical_staff_patients.urls')),
    path('medical_prevention_test/',include('medical_prevention_test.urls')),
    ######################################################### Patient
    
    path('patient_blog/',include('patient_blog.urls')),
    path('patient_blood/',include('patient_blood.urls')),
    path('patient_dashboard/',include('patient_dashboard.urls')),
    path('patient_fullhistory/',include('patient_fullhistory.urls')),
    path('patient_kidsgame/',include('patient_kidsgame.urls')),
    path('patient_mydoctor/',include('patient_mydoctor.urls')),
    path('patient_game/',include('patient_game.urls')),
    path('patient_prevention_test',include('patient_prevention_test.urls')),
    path('patient_gestational_dashboard',include('patient_gestational_dashboard.urls')),

    #########################
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)