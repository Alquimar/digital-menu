from django.db import models
from django.conf import settings
from django.utils.text import slugify
from digital_menu.core.models import AbstractModel
import uuid


class Establishment(AbstractModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="user",
                                related_name="establishment", on_delete=models.PROTECT)
    slug = models.SlugField(null=False, unique=True)
    phone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail', null=True, blank=True, unique=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    address = models.TextField('Endereço')
    logo = models.ImageField(upload_to="establishment/logo", verbose_name="logo", null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + "-" + str(uuid.uuid4())[:4])
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Estabelecimento"
        verbose_name_plural = "Estabelecimentos"
