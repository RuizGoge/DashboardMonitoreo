from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from TBMD import forms
from TBMD.models import EjecucionHoy, Proceso, DetalleEjecucion, Incidente


class FormularioEjecucionHoyView(HttpRequest):

    def index(request):
        ejecucionhoy = forms.FormularioEjecucionHoy()
        return render(request, 'EjecucionHoy.html', {'form': ejecucionhoy})

    def procesar_formulario(request):
        ejecucionhoy = forms.FormularioEjecucionHoy(request.POST)
        if ejecucionhoy.is_valid():
            ejecucionhoy.save()
            ejecucionhoy = forms.FormularioEjecucionHoy()

        return render(request, 'EjecucionHoy.html', {'form': ejecucionhoy, 'mensaje': 'OK'})

    def listar_ejecuciones(request):
        ejecuciones = EjecucionHoy.objects.all()
        return render(request, "ListaEjecuciones.html", {"ejecuciones": ejecuciones})


class FormularioProcesosView(HttpRequest):

    def index(request):
        procesos = forms.FormularioProcesos()
        return render(request, 'Procesos.html', {'form': procesos})

    def procesar_formulario(request):
        procesos = forms.FormularioProcesos(request.POST)
        if procesos.is_valid():
            procesos.save()
            procesos = forms.FormularioProcesos()

        return render(request, 'Procesos.html', {'form': procesos, 'mensaje': 'Proceso registrado'})

    def listar_procesos(request):
        procesos = Proceso.objects.all()
        return render(request, "ListaProcesos.html", {"procesos": procesos})


class FormularioHistoricoProcesosView(HttpRequest):

    def index(request):
        historico = forms.FormularioHistoricoProcesos()
        return render(request, 'Historico.html', {'form': historico})

    def procesar_formulario(request):
        historico = forms.FormularioHistoricoProcesos(request.POST)
        if historico.is_valid():
            historico.save()
            historico = forms.FormularioHistoricoProcesos()

        return render(request, 'Historico.html', {'form': historico, 'mensaje': 'Proceso registrado'})

    def listar_historico(request):
        #ordenar por 1 dia 161 procesos
        historico = DetalleEjecucion.objects.all().order_by('-ID_DETALLE_EJECUCION')[:161]
        return render(request, "ListaHistorico.html", {"historico": historico})


class FormularioIncidentesView(HttpRequest):

    def index(request):
        incidente = forms.FormularioIncidentes()
        return render(request, 'Incidentes.html', {'form': incidente})

    def procesar_formulario(request):
        incidente = forms.FormularioIncidentes(request.POST)
        diccIncidente = request.POST
        fechasolucion_mutada = datetime.strftime(
            datetime.strptime(diccIncidente.get('FECHA_HORA_SOLUCION'), '%Y-%m-%dT%H:%M'), '%Y-%m-%d %H:%M:%S')
        fechareejecucion_mutada = datetime.strftime(
            datetime.strptime(diccIncidente.get('FECHA_HORA_REEJECUCION'), '%Y-%m-%dT%H:%M'), '%Y-%m-%d %H:%M:%S')
        _mutable = diccIncidente._mutable
        diccIncidente._mutable = True
        for llave, valor in diccIncidente.items():
            if llave == 'FECHA_HORA_SOLUCION':
                diccIncidente[llave] = fechasolucion_mutada
            elif llave == 'FECHA_HORA_REEJECUCION':
                diccIncidente[llave] = fechareejecucion_mutada
        #._mutable permite modificar el diccionario que emite el form, por eso se pasa a True
        diccIncidente._mutable = _mutable
        if incidente.is_valid():
            incidente.save()
            incidente = forms.FormularioIncidentes()

        return render(request, 'Incidentes.html', {'form': incidente, 'mensaje': 'Incidente registrado'})

    def listar_incidentes(request):
        incidentes = Incidente.objects.all()
        return render(request, 'ListaIncidentes.html', {"incidentes": incidentes})

    def editar_incidentes(request, id_incidente):
        incidente = Incidente.objects.filter(ID_INCIDENTE=id_incidente).first()
        form = forms.FormularioIncidentesEdit(instance=incidente)
        return render(request, 'IncidenteEdit.html', {'form': form, 'incidente': incidente})

    def actualizar_incidentes(request, id_incidente):
        incidente = Incidente.objects.get(pk=id_incidente)
        form = forms.FormularioIncidentesEdit(request.POST, instance=incidente)
        if form.is_valid():
            form.save()
            incidentes = Incidente.objects.all()
            return render(request, 'ListaIncidentes.html', {"incidentes": incidentes})

    def eliminar_incidentes(request, id_incidente):
        incidente = Incidente.objects.get(pk=id_incidente)
        incidente.delete()
        incidentes = Incidente.objects.all()

        return render(request, 'ListaIncidentes.html', {"incidentes": incidentes, "mensaje": "OK"})



