from django.contrib import admin

from blog_api.models import Comment, Category, PostImages
from blog_api.views import Post

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostImages)