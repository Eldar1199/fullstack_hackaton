# Generated by Django 4.2.5 on 2023-09-25 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_level',
            fields=[
                ('title_of_level', models.CharField(max_length=50, unique=True, verbose_name='Уровень разработчика')),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Job_type',
            fields=[
                ('title_of_type', models.CharField(max_length=50, unique=True, verbose_name='Типы')),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('company_name', models.CharField(max_length=30)),
                ('vacancy', models.CharField(max_length=100)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('salary', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('actuality', models.BooleanField(default=False)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('job_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='post.job_type', verbose_name='Тип направления')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='post.job_level', verbose_name='Уровень разработчика')),
            ],
        ),
    ]
