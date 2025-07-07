from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# مدير المستخدم
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# المستخدم المخصص
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,null=False)
    username = models.CharField(max_length=100,null=False)
    phone = models.IntegerField()
    is_staff = models.BooleanField(default=False)         # صلاحية admin
    is_active = models.BooleanField(default=True)
    is_medical_staff = models.BooleanField(default=False) # هل هو موظف طبي

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "all User"
        verbose_name_plural = "all Users"

class MedicalStaffProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    last_dashboard_check = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Dr. {self.user.username}"    
    

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(MedicalStaffProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='patients')    
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    finger_id  = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField()
    is_approved = models.BooleanField(default=False)  # جديد
    date_of_birth = models.DateField(max_length=20,null=True, blank=True)
    diabetes_type = models.CharField(max_length=50, choices=[
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2'),
        ('Gestational', 'Gestational')
    ])
    # Add other fields like weight, height, etc.
    
    def __str__(self):
        return self.user.username


