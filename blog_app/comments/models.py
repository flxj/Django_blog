
from django.db import models

#博客评论
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
#书评评论
class BookComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey('blog.Book',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
#影评评论
class MovieComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    movie = models.ForeignKey('blog.Movie',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]