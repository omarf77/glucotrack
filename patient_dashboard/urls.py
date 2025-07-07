from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_dashboard,name='patient_dashboard'),
  path('logout/', views.logout_view, name='logout'),

]