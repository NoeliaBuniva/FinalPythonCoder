# Generated by Django 4.1.2 on 2022-11-23 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0014_usuario_delete_fichasocio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
    ]