from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('create',views.create,name='create'),
    path('feed',views.feed,name='feed'),
    path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),
]