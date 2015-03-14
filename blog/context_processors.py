# -*- encoding: utf-8 -*-
from django.utils.encoding import smart_str
from blog.models import Categoria, Post
from taggit.models import Tag

# seta as variaveis abaixo em toda aplicação
def global_vars(request):
    return {
       'categorias': Categoria.objects.all() ,
       'posts_recentes': Post.objects.all().order_by("-criado_em")[:5] ,
       'tags': Tag.objects.all()
    }