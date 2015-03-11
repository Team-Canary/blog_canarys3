# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post, Pagina, Categoria
from django.contrib.syndication.views import Feed

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
        queryset= Post.objects.all().order_by("-criado_em"),
        template_name="blog/blog.html"
    )),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Post,
        template_name="blog/post.html"
    )),

    url(r'^categoria/(?P<pk>\d+)$', 'categoria'),

    url(r'^arquivo$', ListView.as_view(
        queryset= Post.objects.all().order_by("-criado_em"),
        template_name="blog/arquivo.html"
    )),

    url(r'^pagina/(?P<slug>[\w_-]+)$',DetailView.as_view(
        model=Pagina,
        template_name="blog/pagina.html"
    )),

    url(r'^resultado/$','resultado'),

     url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
)
