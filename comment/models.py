from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.post.title + " Comment By " + self.author.username