from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_mydoctor,name='patient_mydoctor'),
  path ('assign-doctor/',views.assign_doctor,name='assign_doctor'),
 

]