# Generated by Django 4.1.2 on 2022-11-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0005_tags_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interests',
            name='tags',
        ),
        migrations.AddField(
            model_name='interests',
            name='tags',
            field=models.ManyToManyField(to='memories.tags'),
        ),
    ]