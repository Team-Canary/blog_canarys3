# -*- encoding: utf-8 -*-
from django.contrib import admin
from blog.models import Categoria, Post, Pagina

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Pagina)