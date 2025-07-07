from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_game,name='patient_game'),

]