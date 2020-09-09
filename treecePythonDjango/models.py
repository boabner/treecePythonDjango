import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


ESTADOCIVIL_CHOICES = (
    ('C', 'Casado(a)'),
    ('S', 'Solteiro(a)'),
    ('D', 'Divorciado(a)'),
    ('V', 'Viúvo(a)'),
)


class Usuario(AbstractUser):
    uuid = models.UUIDField(_('User UUID'), default=uuid.uuid4)

    username = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        unique=True
    )

    email = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    randomNumber = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    estadoCivil = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=ESTADOCIVIL_CHOICES
    )

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('CustomUser')
        verbose_name_plural = _('CustomUsers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CustomUser_detail', kwargs={'pk': self.pk})
