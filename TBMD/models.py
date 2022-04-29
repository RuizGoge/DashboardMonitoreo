from django.db import models


class Proceso(models.Model):
    ID_PROCESO = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_PROCESO')
    NOMBRE_PROCESO = models.CharField(max_length=150, null=True, blank=True)
    TIPO_PROCESO = models.CharField(max_length=50, null=True, blank=True)
    HORA_EJECUCION = models.TimeField()
    PERIODICIDAD = models.CharField(max_length=50, null=True, blank=True)
    SERVIDOR = models.CharField(max_length=50, null=True, blank=True)
    ACTIVO = models.BooleanField(null=True, blank=True)


class DetalleEjecucion(models.Model):
    ID_DETALLE_EJECUCION = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_DETALLE_EJECUCION')
    ID_PROCESO = models.ForeignKey(Proceso, on_delete=models.PROTECT)
    FECHA = models.DateField()
    ESTADO_EJECUCION = models.CharField(max_length=50)

    class Meta:
        ordering = ('-FECHA',)


class EjecucionHoy(models.Model):
    ID_PROCESO = models.IntegerField(primary_key=True)
    FECHA = models.DateField()
    ESTADO_EJECUCION = models.CharField(max_length=50)


class Incidente(models.Model):
    ID_INCIDENTE = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID_INCIDENTE')
    ID_DETALLE_EJECUCION = models.ForeignKey(DetalleEjecucion, on_delete=models.PROTECT)
    PROBLEMA = models.CharField(max_length=500, null=True, blank=True)
    CAUSA = models.CharField(max_length=500, null=True, blank=True)
    IMPACTO = models.CharField(max_length=500, null=True, blank=True)
    SOLUCION = models.CharField(max_length=500, null=True, blank=True)
    FECHA_HORA_SOLUCION = models.DateTimeField(null=True, blank=True)
    RESOLUTOR = models.CharField(max_length=500, null=True, blank=True)
    FECHA_HORA_REEJECUCION = models.DateTimeField(null=True, blank=True)
    ESTADO_REEJECUCION = models.CharField(max_length=50, null=True, blank=True)

# class InfoProceso(models.Model):
