#import os
import markdown
import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import  User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.html import strip_tags

from blog.utils import get_book_info,get_film_info


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #阅读量统计
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


#读书
#fs=FileSystemStorage(location='/static/blog/img/')
class Book(models.Model):
    #书籍信息
    name = models.CharField(max_length=50)

    # 文件流是不会放到数据库里面的，该字段在数据库中只存储路径
    # 参数'upload_to',用于定义上传文件保存的路径(完整的路径为settings.MEDIA_ROOT + upload_to).
    #picture = models.ImageField(storage=fs)

    picture = models.ImageField(upload_to='img',blank=True)
    writer=models.CharField(max_length=50,blank=True)
    publication_date= models.CharField(max_length=20,blank=True)

    #书评
    read_time = models.DateTimeField()  #阅读时间，精确到月吧，改成时间类型便于将来统计
    review=models.TextField(blank=True)
    excerpt = models.CharField(max_length=200)

    created_time = models.DateTimeField(auto_now=True,blank=True)
    modified_time = models.DateTimeField(blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # 如果没有上传图片
        if not self.picture:
            # 则从豆瓣读书获取
            pic,nam,dat=get_book_info(self.name)
            self.picture='img/'+pic
            self.writer=nam
            self.publication_date=dat
        if not self.modified_time:
            self.modified_time=datetime.datetime.now()

        # 调用父类的 save 方法将数据保存到数据库中
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:bookdetail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time']

#电影
class Movie(models.Model):
    #电影信息
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='img', blank=True)
    director=models.CharField(max_length=50,blank=True)
    release_data=models.CharField(max_length=20,blank=True)
    douban_url=models.CharField(max_length=200,blank=True)
    #影评
    watch_time = models.DateTimeField(blank=True)
    review=models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)

    created_time = models.DateTimeField(blank=True)
    modified_time = models.DateTimeField(auto_now=True,blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # 如果没有上传图片
        if not self.picture:
            # 则从豆瓣电影获取
            pic,nam,dat,db=get_film_info(self.name)
            self.picture='img/'+pic
            self.director=nam
            self.release_data=dat
            self.douban_url=db
        if not self.created_time:
            self.created_time=datetime.datetime.now()
        if not self.watch_time:
            self.watch_time=datetime.datetime.now()

        # 调用父类的 save 方法将数据保存到数据库中
        super(Movie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:filmdetail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time']
#杂文
class Essay(models.Model):
    name = models.CharField(max_length=100)
    #
    body=models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']

 #在删除对象前，关联的图片一并删除
@receiver(pre_delete, sender= Book)
def book_file_delete(sender, instance, **kwargs):
    instance.picture.delete(False)

@receiver(pre_delete, sender=Movie)
def film_file_delete(sender, instance, **kwargs):
    instance.picture.delete(False)

"""
创建了一个用户adminuser 31415lxl
"""