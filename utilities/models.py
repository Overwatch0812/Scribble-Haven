from django.db import models

# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=600,null=True,blank=True)
    genre=models.CharField(max_length=100,null=True,blank=True)
    file=models.FileField(upload_to ='uploads/% Y/% m/% d/',null=True,blank=True)
    description=models.TextField()