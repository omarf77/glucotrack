from django.urls import path
from .import views


urlpatterns= [

  path ('',views.staff_dashboard,name='medical_staff_dashboard'),

]