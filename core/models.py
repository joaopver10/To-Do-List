from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    descricao = models.CharField('Descrição', max_length=150, blank=True)


def usuario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.username)

signals.pre_save.connect(usuario_pre_save, sender=Usuario)


