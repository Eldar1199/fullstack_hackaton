

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('vacancy', models.CharField(max_length=30)),

                ('experience', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),

                ('description', models.TextField()),
                ('actuality', models.BooleanField(default=False)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),

                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),

            ],
        ),
    ]
