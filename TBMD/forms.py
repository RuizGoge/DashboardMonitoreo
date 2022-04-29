from django import forms
from TBMD import models


class FormularioEjecucionHoy(forms.ModelForm):
    class Meta:
        model = models.EjecucionHoy
        fields = '__all__'
        widgets = {'FECHA': forms.DateInput(attrs={'type': 'date'})}


class FormularioProcesos(forms.ModelForm):
    class Meta:
        model = models.Proceso
        fields = ('NOMBRE_PROCESO', 'TIPO_PROCESO', 'HORA_EJECUCION', 'PERIODICIDAD', 'SERVIDOR', 'ACTIVO')
        # fields = '__all__'
        widgets = {'HORA_EJECUCION': forms.TimeInput(attrs={'type': 'time'})}


class FormularioHistoricoProcesos(forms.ModelForm):
    CHOICES = (
        ('OK', 'OK'), ('NO OK', 'NOK'), ('NO SE EJECUTA EN ESTE DÍA', 'NO HOY'), ('POR EJECUTAR', 'POR EJECUTAR'))
    ESTADO_EJECUCION = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = models.DetalleEjecucion
        fields = ('ID_PROCESO', 'FECHA', 'ESTADO_EJECUCION')
        # fields = '__all__'
        widgets = {'FECHA': forms.DateInput(attrs={'type': 'date'}), }


class FormularioIncidentes(forms.ModelForm):
    CHOICES = (
        ('OK', 'OK'), ('CARGA MANUAL', 'CARGA MANUAL'))
    ESTADO_REEJECUCION = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = models.Incidente
        fields = (
            'ID_DETALLE_EJECUCION', 'PROBLEMA', 'CAUSA', 'IMPACTO', 'SOLUCION', 'FECHA_HORA_SOLUCION', 'RESOLUTOR',
            'FECHA_HORA_REEJECUCION', 'ESTADO_REEJECUCION')
        # fields = "__all__"
        widgets = {'FECHA_HORA_SOLUCION': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                   'FECHA_HORA_REEJECUCION': forms.DateTimeInput(attrs={'type': 'datetime-local'}, )}


class FormularioIncidentesEdit(forms.ModelForm):
    CHOICES = (
        ('OK', 'OK'), ('CARGA MANUAL', 'CARGA MANUAL'))
    ESTADO_REEJECUCION = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = models.Incidente
        fields = (
            'ID_DETALLE_EJECUCION', 'PROBLEMA', 'CAUSA', 'IMPACTO', 'SOLUCION', 'FECHA_HORA_SOLUCION', 'RESOLUTOR',
            'FECHA_HORA_REEJECUCION', 'ESTADO_REEJECUCION')
        widgets = {'FECHA_HORA_SOLUCION': forms.DateTimeInput(attrs={'type': 'datetime'}),
                   'FECHA_HORA_REEJECUCION': forms.DateTimeInput(attrs={'type': 'datetime'}, )}
