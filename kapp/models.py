from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    purpose=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    query=models.TextField(max_length=250)
    file=models.FileField(upload_to="media/cv/",default=None)
    

