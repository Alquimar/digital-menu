from django.db import models


class AbstractModel(models.Model):
    name = models.CharField('Nome', max_length=100)
    active = models.BooleanField('Ativo(a)?', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True
