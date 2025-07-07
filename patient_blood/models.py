from django.db import models
from homepage.models import PatientProfile

# Create your models here.
class AddEntry(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    blood_sugar = models.PositiveIntegerField()
    date = models.DateField()
    reading_type = models.CharField(max_length=50, choices=[
        ('Fasting', 'Fasting'),
        ('Random', 'Random'),
        ('After Meal', 'After Meal')
    ])
    note = models.TextField(blank=True, null=True)
    
    seen_by_doctor = models.BooleanField(default=False)  # ✅ جديد

    def __str__(self):
            return self.patient.user.username

    class Meta:
        verbose_name = "all Entry"
        verbose_name_plural = "all Entry"