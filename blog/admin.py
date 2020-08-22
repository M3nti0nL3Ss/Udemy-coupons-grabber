from django.contrib import admin
from .models import Post

from django.utils.translation import ugettext_lazy


admin.site.site_title = ugettext_lazy("My TMD Admin")
admin.site.site_header = ugettext_lazy("TMD Administration")
admin.site.index_title = ugettext_lazy("Index")



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author','category')
    #readonly_fields=('author', )
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', '-publish']
    class Media:
        js = ('ckeditor/ckeditor-init.js','ckeditor/ckeditor/ckeditor.js','ckeditor/conf.js')

admin.site.register(Post, PostAdmin)
