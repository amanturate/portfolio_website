from django.db import models

# Create your models here.
class Summary(models.Model):
    summary = models.TextField()

class Job(models.Model):
    resume = models.FileField(upload_to = 'files/',default="")

class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50,default="")
    start_dt = models.DateField()
    end_dt = models.DateField()
    now = models.BooleanField(default = False, help_text = "Check if you are still in the same company" )
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    desc_1 = models.TextField(default="")
    desc_2 = models.TextField(default="",blank=True)
    desc_3 = models.TextField(default="",blank=True)
    start_dt = models.DateField()
    end_dt = models.DateField()
    
class Skill(models.Model):
    name = models.CharField(max_length=25)
    
class Awards(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150, default="")
    Description = models.TextField(default="")
    date = models.DateField()
    cert = models.ImageField(upload_to = 'images/',blank=True)
    award = models.BooleanField(default = False, help_text = "Check if this is award" )
