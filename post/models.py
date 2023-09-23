from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', verbose_name='автор', editable=False)
    company_name = models.CharField(max_length=30, blank=False)
    vacancy = models.CharField(max_length=30, blank=False,unique=True)
    experience = models.PositiveIntegerField(blank=False,default=0)
    salary = models.PositiveIntegerField(blank=False,default=0)
    description = models.TextField(blank=False)
    actuality = models.BooleanField(default=False, blank=False)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    id = models.AutoField(primary_key=True)


    def save(self, *args, **kwargs):
        if not self.author_id:
            self.author = User.objects.get(pk=self.request.user.pk)
        super(Post, self).save(*args, **kwargs)

