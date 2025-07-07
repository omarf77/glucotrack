from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_blog_list,name='patient_blog'),
  path('patient_blog/<int:blog_id>/', views.patient_blog_detail, name='patient_blog_detail'),
]