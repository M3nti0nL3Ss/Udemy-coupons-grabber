# Generated by Django 2.2.5 on 2019-09-25 12:09

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=blog.models.upload_image_path),
        ),
    ]
