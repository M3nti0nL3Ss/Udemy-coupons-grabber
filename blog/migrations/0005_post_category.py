# Generated by Django 2.2.5 on 2019-09-25 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
        ('blog', '0004_auto_20190925_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cat.Category'),
            preserve_default=False,
        ),
    ]
