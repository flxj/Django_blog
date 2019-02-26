from django import template
from ..models import Post, Category,Tag,Book,Movie
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#博文归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_recent_books(num=5):
    return Book.objects.all().order_by('-created_time')[:num]
#图书归档
@register.simple_tag
def book_archives():
    return Book.objects.dates('created_time', 'month', order='DESC')
@register.simple_tag
def get_recent_films(num=5):
    return Movie.objects.all().order_by('-created_time')[:num]
#图书归档
@register.simple_tag
def film_archives():
    return Movie.objects.dates('created_time', 'month', order='DESC')