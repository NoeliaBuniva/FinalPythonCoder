# Generated by Django 4.1.2 on 2022-11-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='entrenamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_muscular', models.CharField(choices=[('TS', 'Tren Superior'), ('TI', 'Tren Inferior'), ('C', 'Core')], max_length=2)),
                ('intensidad', models.CharField(choices=[('alta', 'Alta'), ('media', 'media'), ('baja', 'baja')], max_length=10)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=2)),
            ],
        ),
    ]