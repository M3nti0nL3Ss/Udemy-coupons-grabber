# Generated by Django 2.2.5 on 2019-09-25 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]