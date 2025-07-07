from django.urls import path
from .import views


urlpatterns= [

  path ('',views.medical_staff_patients,name='medical_staff_patients'),
  path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
  path('delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
  path('chat/<int:user_id>/', views.chat, name='chat'),
  path('get-messages/<int:user_id>/', views.get_messages, name='get_messages'),
  path('mark_reading_seen/<int:reading_id>/', views.mark_reading_seen, name='mark_reading_seen'),
  path('mark_all_readings_seen/<int:patient_id>/', views.mark_all_readings_seen, name='mark_all_readings_seen'),
  path('approve_patient/<int:patient_id>/', views.approve_patient, name='approve_patient'),
  path('reject_patient/<int:patient_id>/', views.reject_patient, name='reject_patient'),
  path('bulk-action/', views.bulk_patient_action, name='bulk_patient_action'),

]