# Generated by Django 5.1.1 on 2024-09-15 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
    ]
