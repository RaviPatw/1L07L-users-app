# Generated by Django 5.1.2 on 2024-10-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='banner',
            field=models.ImageField(blank=True, default='register.png', upload_to=''),
        ),
    ]
