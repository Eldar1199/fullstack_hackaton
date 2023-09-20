from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    company_name = models.CharField(max_length=30, blank=False)
    vacancy = models.CharField(max_length=30, blank=False)
    experience = models.PositiveIntegerField(blank=False)
    salary = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    actuality = models.BooleanField(default=False)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)