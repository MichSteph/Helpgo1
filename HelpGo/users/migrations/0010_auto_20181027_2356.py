# Generated by Django 2.1 on 2018-10-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20181027_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, verbose_name='edad'),
        ),
    ]