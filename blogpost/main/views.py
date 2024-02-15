from django.shortcuts import render
from .models import  BlogpostModel  # Import the BlogpostModel model

def home(request):
    blogposts = BlogpostModel.objects.all()
    return render(request, 'home.html', context={'blogposts': blogposts})

def about(request):
    return render(request, 'about.html')
