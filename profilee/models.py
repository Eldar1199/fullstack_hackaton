from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()


class ProfileUser(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles_user')
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Изображение')
    user_resume = models.FileField(upload_to='pdfs/')
    about_user = models.TextField(blank=False)



class ProfileReqruiter(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles_reqruiter')
    company_name = models.TextField()
    location = models.TextField()
    company_phone = models.IntegerField()
    amount_of_emplyees = models.IntegerField()
    about_company = models.TextField()
