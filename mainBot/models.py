from django.db import models

# Create your models here.
class User_Info(models.Model):
    uid = models.CharField(max_length=50, null=False, default='')   
    licenseKey = models.CharField(max_length=50, unique=True, null=False, default='')   
    mdt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uid

class License_Key(models.Model):
    licenseKey = models.CharField(max_length=50, unique=True, null=False, default='')     
    
    def __str__(self):
        return self.key

    