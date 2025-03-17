from django.db import models

# Create your models here.

class patient_info (models.Model):
    Name  = models.CharField(max_length=20, null= False, default= 'Confidential')
    Age   = models.IntegerField(null=False)
    Gender = models.CharField(max_length=10, null=True)
    Disease = models.CharField(max_length=20, null= True)
    bp = models.CharField(max_length=10)
    sugar = models.CharField(max_length= 50)
    oxygen = models.IntegerField()
    status = models.CharField(max_length=20,null= True)