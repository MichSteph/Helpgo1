from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User as User_model
# Create your models here.

class Service(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente_servicio+', verbose_name='cliente')
    service = models.CharField(max_length=50, verbose_name='servicio')
    price = models.IntegerField(verbose_name='precio por hora')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')
    

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return str( self.user )

class Contract(models.Model):
    stts = (
        ('Iniciado', 'Iniciado'),
        ('En proceso', 'En proceso'),
        ('Terminado', 'Terminado'),
    )
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente_contrato+', verbose_name='cliente')
    professional = models.ForeignKey(User_model, on_delete=models.CASCADE, related_name='profesional_contrato+', verbose_name='profesional')
    amount = models.IntegerField(verbose_name='monto')
    service = models.CharField(max_length=50, verbose_name='servicio')
    date = models.DateTimeField(default=now, verbose_name='fecha')
    status = models.CharField(max_length=50, choices=stts, default="Iniciado", verbose_name='estatus')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'
        ordering = ['-created']

    def __str__(self):
        return str( self.client )