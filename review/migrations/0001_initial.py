# Generated by Django 4.2.5 on 2023-09-25 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Содержимое комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='post.post')),
            ],
            options={
                'indexes': [models.Index(fields=['author', 'post'], name='idx_auth_post')],
            },
        ),
        migrations.AddConstraint(
            model_name='favoriteitem',
            constraint=models.UniqueConstraint(fields=('author', 'post'), name='unique_author_post'),
        ),
    ]
