from django.db import models
from core.models.user import User
from core.models.address import Address


class Demmand(models.Model):
    """
    This model contain the DroidPieceDemmand data.
    """

    #Identity
    description = models.CharField(
        max_length=250,
        blank=False,
        verbose_name="Descrição da peça de Droid",
        )

    deliver_address = models.ForeignKey(
        Address,
        on_delete=models.DO_NOTHING,
        verbose_name='Endereço',
    )

    announcer = models.ForeignKey(
        User,
        blank=True,
        help_text="Usuário responsável pela criação do registro (produto).",
        verbose_name="Anunciante",
        on_delete=models.CASCADE,

    )

    # Monitoring
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        verbose_name = "Demanda de Peça de Droid"
        verbose_name_plural = "Demandas de Peça de Droid"

    def __str__(self):
        return "{}".format(self.description)


