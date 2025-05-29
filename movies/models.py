from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
    STATUS_CHOICES = (
        ('Wishlist', 'Wishlist'),
        ('Watched', 'Watched'),
    )

    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(blank=True)
    watched_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
