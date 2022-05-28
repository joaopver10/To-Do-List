from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify


class Tarefa(models.Model):

    descricao = models.CharField('Descrição', max_length=150)

    def __str__(self):
        return self.descricao


class Base(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Usuario(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    senha = models.CharField('Senha', max_length=50)

    def __str__(self):
        return self.nome


def usuario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(usuario_pre_save, sender=Usuario)

def tarefa_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.descricao)

signals.pre_save.connect(tarefa_pre_save, sender=Tarefa)
