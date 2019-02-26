"""blog_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from blog.feed import AllPostsRssFeed

#from django.conf import settings
#from django.conf.urls.static import static

from django.views.static import serve
from blog_app.settings import MEDIA_ROOT,STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^search/', include('haystack.urls')),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

]
