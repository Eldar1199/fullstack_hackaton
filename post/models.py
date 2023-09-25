from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class Job_level(models.Model):
    title_of_level = models.CharField(max_length=50, unique=True,verbose_name='Уровень разработчика')
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_of_level)
        super().save()


class Job_type(models.Model):
    title_of_type = models.CharField(max_length=50, unique=True, verbose_name='Типы')
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_of_type)
        super().save()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', verbose_name='автор', editable=False)
    company_name = models.CharField(max_length=30, blank=False)
    level = models.ForeignKey(Job_level,on_delete=models.SET_NULL,null=True,related_name='level', verbose_name='Уровень разработчика')
    job_type = models.ForeignKey(Job_type, on_delete=models.SET_NULL,null=True,related_name='type', verbose_name='Тип направления')
    vacancy = models.CharField(max_length=100, blank=False)
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

