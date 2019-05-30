from django.db import models
from django.core.exceptions import ValidationError


class Equipo(models.Model):
    """
    Modelo que representa a un cañón o un equipo de música.
    """
    nombre = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)
    fecha_compra = models.DateField()

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    """
    Modelo que representa a una persona que puede retirar un equipo.
    """
    nombre = models.CharField(max_length=250)
    dni = models.CharField(max_length=8)
    materia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Turno(models.Model):
    """
    Modelo que representa a los turnos pedidos por los profesores.
    """
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    referencia_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    referencia_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        formato_fecha = "%d-%m-%y %H:%m"
        fecha_inicio = self.fecha_inicio.strftime(formato_fecha)
        fecha_fin = self.fecha_fin.strftime(formato_fecha)
        return fecha_inicio + "-" + fecha_fin

    def clean(self):
        # import ipdb;ipdb.set_trace()
        # raise ValidationError("no se puede guardar")

        cond1 = Turno.objects.filter(referencia_equipo=self.referencia_equipo, fecha_inicio__lte=self.fecha_inicio,
                                     fecha_fin__gte=self.fecha_inicio).count()

        cond2 = Turno.objects.filter(referencia_equipo=self.referencia_equipo, fecha_inicio__lte=self.fecha_fin,
                                     fecha_fin__gte=self.fecha_fin).count()

        cond3 = self.fecha_fin <= self.fecha_inicio

        if cond3:
            raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")
        elif cond1 != 0 or cond2 != 0:
            raise ValidationError("No se puede reservar el equipo para la fecha seleccionada.")