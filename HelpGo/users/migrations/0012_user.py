# Generated by Django 2.1 on 2018-10-28 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_auto_20181028_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True, verbose_name='edad')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users', verbose_name='imagen')),
                ('area', models.CharField(blank=True, choices=[('Programador', 'Programador'), ('Contador', 'Contador'), ('Arquitecto', 'Arquitecto'), ('Carpintero', 'Carpintero')], max_length=100, null=True, verbose_name='area')),
                ('active', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10, verbose_name='activo')),
                ('description', models.TextField(verbose_name='descripcion')),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
                ('username', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]