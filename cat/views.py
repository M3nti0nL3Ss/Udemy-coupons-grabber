from django.shortcuts import render
from .models import Category
from django.views.generic import TemplateView
from blog.models import Post
from django.views.generic import DetailView


class CategoryList(TemplateView):
    template_name = "cat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

class CategoryDetail(DetailView):
    model = Category
    template_name = "cat_posts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().filter(category_id=kwargs['object'].id, status='published')
        context['cats'] = Category.objects.all()
        return context