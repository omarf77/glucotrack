
from django.db import models
from homepage.models import MedicalStaffProfile

class BlogPost(models.Model):
    doctor = models.ForeignKey(MedicalStaffProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title