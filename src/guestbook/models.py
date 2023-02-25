from django.db import models
from django.utils.translation import gettext_lazy as _


class GuestBook(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Активно')
        BLOCKED = 'blocked', _('Заблокировано')

    author = models.CharField(max_length=256, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(max_length=1024, null=False, blank=False, verbose_name='Почта автора')
    description = models.TextField(max_length=4096, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
