from django.urls import path
from .import views


urlpatterns= [

  path ('',views.gestational_dashboard,name='gestational_dashboard'),
 
]