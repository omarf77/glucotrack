from django.contrib import admin
from .models import AddEntry
from homepage.models import PatientProfile  # تأكد أنك مستورد PatientProfile




# Register your models here.
@admin.register(AddEntry)
class AddEntryAdmin(admin.ModelAdmin):
    model = AddEntry
    list_display = ('patient_name', 'blood_sugar', 'date', 'reading_type', 'note_preview')
    list_filter = ('reading_type', 'date')
    search_fields = ('patient__user__username', 'patient__user__email', 'note')
    
    def patient_name(self, obj):
        return obj.patient.user.username

    def note_preview(self, obj):
        return obj.note[:30]  # عرض أول 30 حرف من الملاحظة
    











