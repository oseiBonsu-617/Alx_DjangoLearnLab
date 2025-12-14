from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(default="Hello there!")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name='following')


    def __str__(self):
        return f"{self.username}"