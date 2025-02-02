from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='register.png', blank=True)

    def __str__(self):
        return self.username
