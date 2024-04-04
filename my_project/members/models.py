from django.db import models

# Create your models here.

class Exhibit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exhibit_images/')
