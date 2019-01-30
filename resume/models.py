from django.db import models

# Create your models here.
class OnlyImage(models.Model):
    image = models.ImageField(upload_to='profile_image',blank = True)
    gif = models.ImageField(upload_to='profile_image',blank=True)
    