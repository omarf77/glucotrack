from django.urls import path
from .import views


urlpatterns= [

  path ('',views.patient_full_history,name='patient_fullhistory'),
  path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),


]