# Generated by Django 4.1.2 on 2022-10-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
