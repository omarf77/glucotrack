from django.urls import path
from .import views


urlpatterns= [

  path ('',views.medical_staff_addblog,name='medical_staff_addblog'),

]