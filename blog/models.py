from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length =40, help_text='Title of Blog')
    pub_date = models.DateField()
    body = models.CharField(max_length =200, help_text='Blog post')
    image = models.ImageField(upload_to = 'images/')
