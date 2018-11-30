# Generated by Django 2.1 on 2018-11-25 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='monto')),
                ('service', models.CharField(max_length=50, verbose_name='servicio')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha')),
                ('status', models.CharField(choices=[('Iniciado', 'Iniciado'), ('En proceso', 'En proceso'), ('Terminado', 'Terminado')], default='Iniciado', max_length=50, verbose_name='estatus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente+', to=settings.AUTH_USER_MODEL, verbose_name='cliente')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesional+', to=settings.AUTH_USER_MODEL, verbose_name='profesional')),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contratos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50, verbose_name='servicio')),
                ('price', models.IntegerField(verbose_name='precio por hora')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente+', to=settings.AUTH_USER_MODEL, verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]
