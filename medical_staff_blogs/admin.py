
from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'doctor', 'created_at')
    search_fields = ('title', 'short_description', 'doctor__username')
    list_filter = ('created_at',)