from blog.models import Post
from cat.models import Category

for cat in Category.objects.all():
        for tag in cat.tags.all():
            Post.objects.search(tag).update(category_id=cat.id)

