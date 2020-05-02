from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'body','author', 'created', 'updated', 'approved']
    list_filter = ('post','author','approved',)

admin.site.register(Comment, CommentAdmin)