from django.db import models

# Create your model here
class Appoint_details(models.Model):
    careType=models.CharField(max_length=40)
    location=models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    dateOfAppointment = models.CharField(max_length=50)
    timeOfAppoinment= models.CharField(max_length=30)
    fullname=models.CharField(max_length=50)
    phone = models.BigIntegerField()
    Status=models.CharField(max_length=50,default="Pending")

