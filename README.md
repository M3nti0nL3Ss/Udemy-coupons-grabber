# Udemy-coupons-grabber
## Installing
### Pre
virtualenv
python 3
django
pip
### run
git clone https://github.com/M3nti0nL3Ss/Udemy-coupons-grabber.git
virtualenv env && source env/bin/activate
pip install -r req*
python manage.py makemigrations; python manage.py migrate # if it didn't work replace the the snippet bellow

```
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE,default=lambda: Category.objects.get(id=1))
    image = models.ImageField(upload_to=upload_image_path)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE,default=lambda: User.objects.get(id=1))
```
By
```
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
```

DEMO: https://www.th3md.com
