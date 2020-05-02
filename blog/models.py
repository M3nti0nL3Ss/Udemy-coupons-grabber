from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cat.models import Category
import os
import random
from datetime import datetime
from django.db.models import Q

class PostQuerySet(models.query.QuerySet):
    def status(self):
        return self.filter(status="published")

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(body__icontains=query)
                  )
        # M3nti0nL3Ss
        return self.filter(lookups).distinct()

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().status()


    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().status().search(query)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    timestamp = datetime.timestamp(datetime.now())
    final_filename = '{}_{}{}'.format(timestamp, new_filename, ext)
    return "posts/{}".format(final_filename)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE,default=lambda: Category.objects.get(id=1))
    image = models.ImageField(upload_to=upload_image_path)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE,default=lambda: User.objects.get(id=1))
    body = models.TextField()
    link = models.CharField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    objects = PostManager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/post/{}/{}/{}".format(self.created.year, self.created.month, self.slug)

