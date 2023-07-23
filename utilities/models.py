from django.db import models
from account.models import CustomUser
# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=600,null=True,blank=True)
    author=models.CharField(max_length=100,null=True,blank=True)
    genre=models.CharField(max_length=100,null=True,blank=True)
    file=models.FileField(upload_to ='images/',null=True,blank=True)
    description=models.TextField()


    def __str__(self):
        return self.title

class upload_image(models.Model):
    blogs=models.ForeignKey(blog,on_delete=models.CASCADE,null=True,blank=True)
    img=models.ImageField(upload_to ='images/',null=True,blank=True)
