from django.db import models

# Create your models here.

class Exhibit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exhibit_images/')

    playtypePhysical = models.TextField(blank=True, null=True)
    playtypeSocialEmotional = models.TextField(blank=True, null=True)
    playtypeSensory = models.TextField(blank=True, null=True)
    playtypeCognitive = models.TextField(blank=True, null=True)
    playtypeCommunication = models.TextField(blank=True, null=True)

class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    image = models.ImageField(upload_to='exhibit_images/')