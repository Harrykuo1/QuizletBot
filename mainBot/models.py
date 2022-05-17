from ast import alias
from django.db import models

# Create your models here.
class user_info(models.Model):
    uid = models.CharField(max_length=50, null=False, default='')   
    licenseKey = models.CharField(max_length=50, unique=True, null=False, default='')   
    mdt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uid

class license_key(models.Model):
    licenseKey = models.CharField(max_length=50, unique=True, null=False, default='')     
    
    def __str__(self):
        return self.key

class label_url(models.Model):
    uid = models.CharField(max_length=50, null=False, default='')   
    labelName = models.CharField(max_length=30, null=False, default='')   
    url = models.CharField(max_length=200, null=False, default='')  
    mdt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uid  

class global_label_url(models.Model): 
    labelName = models.CharField(max_length=50, null=False, default='')   
    url = models.CharField(max_length=200, null=False, default='')  
    mdt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uid  


    