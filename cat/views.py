from django.shortcuts import render
from .models import Category
from django.views.generic import TemplateView
from blog.models import Post
from django.views.generic import DetailView

from django.views.generic.list import MultipleObjectMixin

from client.views import get_client_infos

class CategoryList(TemplateView):
    template_name = "cat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

class CategoryDetail(DetailView, MultipleObjectMixin):
    model = Category
    template_name = "cat_posts.html"
    paginate_by = 9
    def get_context_data(self, **kwargs):
        get_client_infos(self.request)
        object_list = Post.objects.all().filter(category_id=self.object.id, status='published')
        context = super(CategoryDetail,self).get_context_data(object_list=object_list,**kwargs)
        context['cats'] = Category.objects.all()
        return context
