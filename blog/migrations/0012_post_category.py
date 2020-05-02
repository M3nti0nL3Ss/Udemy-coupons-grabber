# Generated by Django 2.2.5 on 2019-09-25 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
        ('blog', '0011_remove_post_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='cat.Category'),
            preserve_default=False,
        ),
    ]
