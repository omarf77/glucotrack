from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_kidsgame,name='patient_kidsgame'),

]