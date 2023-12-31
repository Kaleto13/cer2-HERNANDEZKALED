# Generated by Django 4.2.6 on 2023-10-22 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidades',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('detalle', models.CharField(max_length=255)),
                ('detalle_corto', models.CharField(max_length=126)),
                ('eleccion_tipo', models.CharField(choices=[('S', 'Suspencion de actividades'), ('C', 'Suspencion de clases'), ('I', 'Informacion')], default='I', max_length=1)),
                ('fecha_publicacion', models.DateField()),
                ('fecha_modificacion', models.DateTimeField()),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='miapp.entidades')),
            ],
        ),
    ]
