# Generated by Django 4.1.2 on 2022-11-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0010_remove_entrenamientos_ejercicios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios',
            name='clase',
            field=models.CharField(choices=[('Yoga', 'Yoga'), ('Meditación', 'Meditación')], max_length=20),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='horario',
            field=models.CharField(choices=[('8hs', '8 hs'), ('9hs', '9 hs'), ('10hs', '10 hs'), ('11hs', '11 hs'), ('12hs', '12 hs')], max_length=5),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='sede',
            field=models.CharField(choices=[('Belgrano', 'Belgrano'), ('Nuñez', 'Nuñez'), ('Palermo', 'Palermo')], max_length=20),
        ),
    ]
