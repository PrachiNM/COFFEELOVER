from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=50, default=None)
    lastname = models.CharField(max_length=50, default=None)
    emailid = models.EmailField(unique=True)
    password = models.TextField(max_length=32)
    image = models.ImageField(upload_to='pics', default=None)
