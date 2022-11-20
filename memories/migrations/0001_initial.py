# Generated by Django 4.1.2 on 2022-10-30 10:51

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
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('place', models.CharField(max_length=15)),
                ('history', models.DateTimeField()),
                ('ftravel', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('video', models.FileField(blank=True, upload_to='')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('pu', 'عمومی'), ('pr', 'خصوصی')], default='pr', max_length=2)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
