# Generated by Django 4.1.2 on 2022-11-16 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0005_rutina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenamientos',
            name='intensidad',
        ),
    ]
