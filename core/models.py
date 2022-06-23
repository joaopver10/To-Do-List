from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class Tarefa(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tarefa = models.CharField('Descrição', max_length=150)

    def __str__(self):
        return self.tarefa

def tarefa_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.tarefa)


signals.pre_save.connect(tarefa_pre_save, sender=Tarefa)


