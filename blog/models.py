# -*- encoding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager

from django.db.models import signals
from django.template.defaultfilters import slugify

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __unicode__(self):
        return self.categoria

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    corpo = models.TextField()
    criado_em = models.DateTimeField()
    tags = TaggableManager()
    categoria = models.ManyToManyField('blog.Categoria')
    imagemDestacada = models.ImageField()
    slug = models.SlugField(max_length=100, blank=True)

    def __unicode__(self):
        return self.titulo

class Pagina(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    titulo = models.CharField(max_length=100)
    corpo = models.TextField()
    criado_em = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.titulo

# função de geração do slug
def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(slug_pre_save, sender=Post)
signals.pre_save.connect(slug_pre_save, sender=Pagina)