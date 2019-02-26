from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

    url(r'^book/$', views.BookView.as_view(), name='book'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='bookdetail'),
    url(r'^book/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.BookArchivesView.as_view(), name='book'),

    url(r'^film/$', views.FilmView.as_view(), name='film'),
    url(r'^film/(?P<pk>[0-9]+)/$', views.FilmDetailView.as_view(), name='filmdetail'),
    url(r'^film/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.FilmArchivesView.as_view(), name='film'),

    url(r'^about/$', views.about, name='about'),
]