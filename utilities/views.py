from django.shortcuts import render,redirect
from .models import blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def create(request):
    if request.method=='POST':
        title=request.POST['title']
        genre=request.POST['genre']
        description=request.POST['description']
        blogs=blog()
        blogs.title=title
        blogs.genre=genre
        blogs.description=description
        blogs.save()
        return redirect('home')
    elif 'file' in request.FILES:
        title=request.POST['title']
        genre=request.POST['genre']
        file=request.FILES['file']
        description=request.POST['description']
        blogs=blog()
        blogs.title=title
        blogs.genre=genre
        blogs.file=file
        blogs.description=description
        blogs.save()
        return redirect('home')
    else:
        return render(request,'create.html')

def feed(request):
    feed=blog.objects.all()
    return render(request,'feeds.html',{'feeds':feed})