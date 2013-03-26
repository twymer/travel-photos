from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
