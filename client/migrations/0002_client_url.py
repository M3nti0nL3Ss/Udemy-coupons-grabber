# Generated by Django 3.0.5 on 2020-05-11 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='url',
            field=models.CharField(blank=True, default='none', max_length=100),
        ),
    ]