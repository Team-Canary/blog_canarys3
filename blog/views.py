# -*- encoding: utf-8 -*-
from blog.models import Post, Categoria
from django.shortcuts import render_to_response

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("blog/tagpage.html", {"posts":posts, "tag":tag})

def categoria(request, pk):
    categoria = Categoria.objects.get(pk = pk)
    posts = Post.objects.filter(categoria__id = pk).select_related()
    return render_to_response("blog/categoria.html", {"posts":posts, 'categoria': categoria})

def resultado(request):
    pesquisa = request.GET.get('resultado')
    posts = Post.objects.filter(corpo__contains = pesquisa)
    return render_to_response("blog/resultado.html", {"posts":posts, "pesquisa": pesquisa})