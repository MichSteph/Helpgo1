# Generated by Django 2.1 on 2018-10-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20181027_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
