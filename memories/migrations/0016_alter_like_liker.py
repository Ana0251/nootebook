# Generated by Django 4.1.2 on 2022-11-15 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memories', '0015_alter_like_memory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='liker',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
