from django.db import models

# Create your models here.
class photosgallery(models.Model):
    img = models.ImageField(upload_to='dynamicpic')