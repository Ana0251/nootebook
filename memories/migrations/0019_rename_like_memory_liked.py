# Generated by Django 4.1.2 on 2022-11-15 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0018_remove_memory_like_memory_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memory',
            old_name='like',
            new_name='liked',
        ),
    ]
