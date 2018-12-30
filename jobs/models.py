from django.db import models

# Create your models here.
class Summary(models.Model):
    summary = models.TextField()

class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length = 200)

class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50,default="")
    start_dt = models.DateField()
    end_dt = models.DateField()
    now = models.BooleanField(default = False, help_text = "Check if you are still in the same company" )
