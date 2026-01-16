from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # ❗ если логин по email — username убираем
    username = None

    email = models.EmailField(
        _('email address'),
        unique=True
    )

    phone = models.CharField(
        _('Телефон'),
        max_length=15,
        blank=True,
        null=True
    )

    is_married = models.BooleanField(
        _('Женат / Замужем'),
        default=False
    )

    age = models.PositiveSmallIntegerField(
        _('Возраст'),
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
