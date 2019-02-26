from django.conf.urls import url

from . import views
app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'^comment/book/(?P<book_pk>[0-9]+)/$', views.book_comment, name='book_comment'),
    url(r'^comment/film/(?P<film_pk>[0-9]+)/$', views.film_comment, name='film_comment'),
]