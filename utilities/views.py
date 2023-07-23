from django.shortcuts import render,redirect
from .models import blog
from account.models import CustomUser

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def create(request):
    if request.method=='POST':
        if 'img' in request.FILES:
            title=request.POST['title']
            authorz=request.POST['authorz']
            genre=request.POST['genre']
            description=request.POST['description']
            file=request.FILES['img']
            blogs=blog()
            blogs.title=title
            blogs.author=authorz
            blogs.genre=genre
            blogs.file=file
            blogs.description=description
            blogs.save()
            return redirect('feed')
        else:
            title=request.POST['title']
            author=request.POST['author']
            genre=request.POST['genre']
            description=request.POST['description']
            blogs=blog()
            blogs.title=title
            blogs.author=authorz
            blogs.genre=genre
            blogs.description=description
            blogs.save()
            return redirect('feed')
    else:
        user= CustomUser.objects.get(id=request.user.id)
        return render(request,'create.html',{'Users':user})

def feed(request):
    feed=blog.objects.all()
    return render(request,'feeds.html',{'feeds':feed})

def blog_detail(request,id):
    detail=blog.objects.get(id=id)
    return render(request,'blog.html',{'blog':detail})

def edit_blog(request,id):
    if request.method=='POST':
        if 'sahil' in request.FILES:
            title=request.POST['title']
            author=request.POST['author']
            genre=request.POST['genre']
            description=request.POST['description']
            filez=request.FILES['sahil']
            blogs=blog.objects.get(id=id)
            blogs.title=title
            blogs.author=author
            blogs.genre=genre
            blogs.file=filez
            blogs.description=description
            blogs.save()
            return redirect('feed')
        else:
            title=request.POST['title']
            author=request.POST['author']
            genre=request.POST['genre']
            description=request.POST['description']
            blogs=blog.objects.get(id=id)
            blogs.title=title
            blogs.author=author
            blogs.genre=genre
            blogs.description=description
            blogs.save()
            return redirect('feed')
    else:
        blogs=blog.objects.get(id=id)
        return render(request,'edit_blog.html',{'blogs':blogs})

def account(request):
    account=CustomUser.objects.get(id=request.user.id)
    blogz=blog.objects.filter(author=request.user.name)
    countz=blogz.count()
    return render(request,'account.html',{'accounts':account,'blogs':blogz,'count':countz})


