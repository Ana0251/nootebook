# Generated by Django 4.1.2 on 2022-11-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0014_alter_like_memory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='memory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='memories.memory'),
        ),
    ]
