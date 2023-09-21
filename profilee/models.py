from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileUser(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                related_name='profiles_user', 
                                primary_key=True, 
                                verbose_name='Пользователь')
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Изображение', blank=True)
    user_resume = models.FileField(upload_to='pdfs/', blank=True, verbose_name='Файлы')
    about_user = models.TextField(blank=True, verbose_name='О человеке')
    company_name = models.TextField(blank=True, verbose_name='Компания')
    location = models.TextField(blank=True, verbose_name='Адрес')
    company_phone = models.PositiveIntegerField(blank=True, null=True, verbose_name='Телефон', default=0)
    amount_of_emplyees = models.IntegerField(blank=True, null=True, verbose_name='Количество людей', default=0)
    about_company = models.TextField(blank=True, verbose_name='О компании')
