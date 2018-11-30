from django.db import models
from django.conf import settings
from django.contrib.auth.models import User as User_model
from django.db.models.signals import post_save
# Create your models here.

class User(models.Model):
    Activated = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    Areas = (
        ('Programador', 'Programador'),
        ('Contador', 'Contador'),
        ('Arquitecto', 'Arquitecto'),
        ('Carpintero', 'Carpintero'),
        ('Coreografo/a', 'Coreografo/a'),
        ('Medico', 'Medico'),
        ('Entrenador personal', 'Entrenador personal'),
        ('Herrero', 'Herrero'),
    )
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    age = models.IntegerField(verbose_name='edad', null=True)
    image = models.ImageField(upload_to='users', null=True, blank=True, verbose_name='imagen')
    area = models.CharField(max_length=100, choices=Areas, null=True, blank=True, verbose_name='area')
    active = models.CharField(max_length=10, choices=Activated, default='no', verbose_name='activo')
    description = models.TextField(verbose_name='descripcion')
    score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.username = request.user
    #     super().save_model(request, obj, form, change)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user = User.objects.create(username=kwargs['instance'])

    post_save.connect(create_profile, sender=User_model)

    def __str__(self):
        return str( self.pk)
    