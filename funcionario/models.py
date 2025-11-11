from django.db import models

class Funcionarios(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Nome'
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Sobrenome'
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        verbose_name='CPF',
        unique=True
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name='Tempo de Serviço (anos)'
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Remuneração'
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'