from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_prevention_test,name='patient_prevention_test'),

]