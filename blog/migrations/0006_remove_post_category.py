# Generated by Django 2.2.5 on 2019-09-25 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]