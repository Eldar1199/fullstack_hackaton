

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion




class Migration(migrations.Migration):

    initial = True

    dependencies = [


        ('account', '0001_initial'),


    ]

    operations = [
        migrations.CreateModel(
            name='ProfileReqruiter',
            fields=[


                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles_reqruiter', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Работодатель')),
                ('company_name', models.TextField(blank=True, verbose_name='Компания')),
                ('location', models.TextField(blank=True, verbose_name='Адрес')),
                ('company_phone', models.IntegerField(blank=True, verbose_name='Телефон')),
                ('amount_of_emplyees', models.IntegerField(blank=True, verbose_name='Количество людей')),
                ('about_company', models.TextField(blank=True, verbose_name='О компании')),


            ],
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[


                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles_user', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение')),
                ('user_resume', models.FileField(blank=True, upload_to='pdfs/', verbose_name='Файлы')),
                ('about_user', models.TextField(blank=True, verbose_name='О человеке')),

            ],
        ),
    ]
