# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover();

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_canarys3.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^blog/admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
