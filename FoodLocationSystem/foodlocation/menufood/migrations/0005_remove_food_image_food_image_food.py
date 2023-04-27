# Generated by Django 4.1.7 on 2023-04-27 08:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menufood', '0004_alter_food_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
        migrations.AddField(
            model_name='food',
            name='image_food',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, null=True, verbose_name='image_food'),
        ),
    ]