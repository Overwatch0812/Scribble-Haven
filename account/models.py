from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username=None
    name= models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    contact_num=models.CharField(max_length=10,null=True,blank=True)
    

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[] 
