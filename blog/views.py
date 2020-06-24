from django.shortcuts import render, get_object_or_404
from .models import blog_project


# Create your views here.
def all_blogs(request):
	blogs = blog_project.objects.order_by('-date')
	return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
	blogse = get_object_or_404(blog_project,pk = blog_id)
	return render(request,'blog/detail.html',{'blogse':blogse})


