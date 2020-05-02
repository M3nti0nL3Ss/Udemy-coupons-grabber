from django.contrib import admin
from .models import Category
from django.db.models import Count
from blog.models import Post


class CategoryAdmin(admin.ModelAdmin):
    def posts_count(self,request):
        return Post.objects.all().filter(category_id=request).count()
    
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','description', 'slug','posts_count')

admin.site.register(Category, CategoryAdmin)

