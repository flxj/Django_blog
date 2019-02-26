
from django.contrib import admin
from .models import Post, Category, Tag, Book,Movie

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time', 'modified_time', 'author']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time', 'modified_time', 'author']

# 把新增的 XXXAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
admin.site.register(Tag)

#使得这些对象可以在管理页面显示