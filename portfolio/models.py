from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = CloudinaryField('image')