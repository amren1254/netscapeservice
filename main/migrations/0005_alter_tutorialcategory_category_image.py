# Generated by Django 5.0.2 on 2024-02-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tutorialcategory_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='main/category_images/'),
        ),
    ]
