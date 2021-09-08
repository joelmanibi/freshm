# Generated by Django 3.2.5 on 2021-09-08 13:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210830_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='etat_stock',
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image_produit',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
