import uuid
from django.db import models
from django.utils import timezone


class Guest(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        verbose_name='Nome do convidado',
        max_length=200
    )
    confirmed = models.BooleanField(
        verbose_name="Confirmado?",
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
    confirmed_at = models.DateTimeField(
        verbose_name="Data de confirmação",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "guest"
        verbose_name_plural = "guests"
        db_table = "tb_guests"


