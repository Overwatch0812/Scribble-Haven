from django.shortcuts import render,redirect
from .models import blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def create(request):
    if request.method=='POST':
        if 'img' in request.FILES:
            title=request.POST['title']
            genre=request.POST['genre']
            description=request.POST['description']
            file=request.FILES['img']
            blogs=blog()
            blogs.title=title
            blogs.genre=genre
            blogs.file=file
            blogs.description=description
            blogs.save()
            return redirect('feed')
        else:
            title=request.POST['title']
            genre=request.POST['genre']
            description=request.POST['description']
            blogs=blog()
            blogs.title=title
            blogs.genre=genre
            blogs.description=description
            blogs.save()
            return redirect('feed')
    else:
        return render(request,'create.html')

def feed(request):
    feed=blog.objects.all()
    return render(request,'feeds.html',{'feeds':feed})

def blog_detail(request,id):
    detail=blog.objects.get(id=id)
    return render(request,'blog.html',{'blog':detail})
