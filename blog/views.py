from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from blog.models import Post
from django.views.generic import DetailView
from cat.models import Category
from comment.models import Comment
from cms0.forms import CommentForm

from django.views.generic import ListView




class HomePageView(ListView):

    template_name = "home.html"
    paginate_by = 9
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context




class PostDetail(DetailView):
    model = Post
    template_name = "detail.html"
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['comments'] = Comment.objects.all().filter(post=self.get_object(),approved=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
        else:
            form = None
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
                #comment.email = request.user.email
                #comment.author_id = 0
            comment.save()
            return redirect(post.get_absolute_url())
        context = self.get_context_data(object=post)
        context['comment_form'] = form
        return self.render_to_response(context)







