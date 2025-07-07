from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from homepage.models import MedicalStaffProfile
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='login')
def medical_staff_blogs(request):
    doctor_profile = get_object_or_404(MedicalStaffProfile, user=request.user)
    blogs = BlogPost.objects.filter(doctor=doctor_profile).order_by('-created_at')
    return render(request, 'Medical/blogs.html', {'blog_posts': blogs})


@login_required(login_url='login')
def add_blog(request):
    doctor_profile = get_object_or_404(MedicalStaffProfile, user=request.user)

    if request.method == 'POST':
        title = request.POST['title']
        short_description = request.POST['short_description']
        content = request.POST['content']
        image = request.FILES.get('image')

        BlogPost.objects.create(
            doctor=doctor_profile,
            title=title,
            short_description=short_description,
            content=content,
            image=image,
            created_at=timezone.now()
        )
        return redirect('medical_staff_blogs')

    return render(request, 'Medical/add_blog.html')


@login_required(login_url='login')
def edit_blog(request, blog_id):
    doctor_profile = get_object_or_404(MedicalStaffProfile, user=request.user)
    blog = get_object_or_404(BlogPost, id=blog_id, doctor=doctor_profile)

    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.short_description = request.POST['short_description']
        blog.content = request.POST['content']

        if request.FILES.get('image'):
            blog.image = request.FILES['image']

        blog.save()
        return redirect('medical_staff_blogs')

    return render(request, 'Medical/edit_blog.html', {'blog': blog})


@login_required(login_url='login')
def delete_blog(request, blog_id):
    doctor_profile = get_object_or_404(MedicalStaffProfile, user=request.user)
    blog = get_object_or_404(BlogPost, id=blog_id, doctor=doctor_profile)
    blog.delete()
    return redirect('medical_staff_blogs')
