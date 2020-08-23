# Generated by Django 3.0.5 on 2020-05-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(blank=True, max_length=100)),
                ('agent', models.CharField(blank=True, max_length=500)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('country_code', models.CharField(blank=True, max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('region_name', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=100)),
                ('lat', models.CharField(blank=True, max_length=100)),
                ('lon', models.CharField(blank=True, max_length=100)),
                ('timezone', models.CharField(blank=True, max_length=100)),
                ('isp', models.CharField(blank=True, max_length=100)),
                ('org', models.CharField(blank=True, max_length=100)),
                ('ass', models.CharField(blank=True, max_length=100)),
                ('host', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]