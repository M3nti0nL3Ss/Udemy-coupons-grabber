from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from cat.models import Category

from client.views import get_client_infos

class SearchPostView(ListView):
    template_name = "search.html"
    paginate_by = 9
    def get_context_data(self, *args, **kwargs):
        get_client_infos(self.request)
        context = super(SearchPostView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['cats'] = Category.objects.all()
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Post.objects.search(query)
        return Post.objects.all()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''
