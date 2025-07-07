from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,PatientProfile,MedicalStaffProfile
from patient_blood.models import AddEntry  
from medical_staff_blogs.models import BlogPost


class BlogInline(admin.TabularInline):
    model = BlogPost
    extra = 0  # ما يظهر صفوف فاضية
    fields = ('title', 'short_description', 'created_at')
    readonly_fields = ('created_at',)
    can_delete = False 

class AddEntryInline(admin.TabularInline):
        model = AddEntry
        extra = 0
        readonly_fields = ['blood_sugar', 'date', 'reading_type', 'note']
        can_delete = False 

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','get_email','gender', 'age', 'diabetes_type', 'finger_id')
    search_fields = ('username', 'email')
    list_filter = ('gender', 'diabetes_type')
    inlines = [AddEntryInline]
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    
    
   


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active', 'is_medical_staff')
    

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff','is_medical_staff','is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'is_medical_staff')}
        ),
    )

    search_fields = ('email', 'username', 'phone ')
    ordering = ('email',)

@admin.register(MedicalStaffProfile)
class MedicalStaffProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'is_staff', 'is_active', 'is_medical_staff']
    search_fields = ['user__username', 'user__email', 'user__phone']
    inlines = [BlogInline]
    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def phone(self, obj):
        return obj.user.phone
    
    def is_staff(self, obj):
        return obj.user.is_staff

    def is_active(self, obj):
        return obj.user.is_active

    def is_medical_staff(self, obj):
        return obj.user.is_medical_staff
    
