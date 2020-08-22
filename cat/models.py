from django.db import models

from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    slug = models.SlugField()
    tags = TaggableManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/cat/{}".format(self.slug)
