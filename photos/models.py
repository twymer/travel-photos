from django.db import models

class Photo(models.Model):
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
