from django.urls import path
from .import views


urlpatterns= [

  path ('',views.medical_prevention_test,name='medical_prevention_test'),

]