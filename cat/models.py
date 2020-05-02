from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/cat/{}".format(self.slug)