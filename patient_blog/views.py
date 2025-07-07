from django.shortcuts import render, get_object_or_404
from medical_staff_blogs.models import BlogPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def patient_blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'Patient/blog.html', {'blogs': blogs})

@login_required(login_url='login')
def patient_blog_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'Patient/blog_detail.html', {'blog': blog})
