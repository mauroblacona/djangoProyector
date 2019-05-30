# Generated by Django 2.0.4 on 2019-04-16 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('tipo', models.CharField(max_length=250)),
                ('fecha_compra', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('dni', models.CharField(max_length=8)),
                ('materia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('referencia_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipo')),
                ('referencia_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.Profesor')),
            ],
        ),
    ]
