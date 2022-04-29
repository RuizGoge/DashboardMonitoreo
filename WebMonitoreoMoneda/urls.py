"""WebMonitoreoMoneda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from TBMD.views import FormularioEjecucionHoyView, FormularioProcesosView, FormularioHistoricoProcesosView, \
    FormularioIncidentesView
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('insertarEjecuciones/', FormularioEjecucionHoyView.index, name='insertarEjecuciones'),
    path('guardarEjecucionHoy/', FormularioEjecucionHoyView.procesar_formulario, name='guardarEjecucion'),
    path('listarEjecuciones/', FormularioEjecucionHoyView.listar_ejecuciones, name='listarEjecuciones'),
    path('insertarProcesos/', FormularioProcesosView.index, name='insertarProceso'),
    path('guardarProcesos/', FormularioProcesosView.procesar_formulario, name='guardarProceso'),
    path('listarProcesos/', FormularioProcesosView.listar_procesos, name='listarProcesos'),
    path('insertarHistorico/', FormularioHistoricoProcesosView.index, name='insertarHistorico'),
    path('guardarHistorico/', FormularioHistoricoProcesosView.procesar_formulario, name='guardarHistorico'),
    path('listarHistorico/', FormularioHistoricoProcesosView.listar_historico, name='listarHistorico'),
    path('insertarIncidente/', FormularioIncidentesView.index, name='insertarIncidente'),
    path('guardarIncidente/', FormularioIncidentesView.procesar_formulario, name='guardarIncidente'),
    path('listarIncidentes/', FormularioIncidentesView.listar_incidentes, name='listarIncidentes'),
    path('editarIncidente/<int:id_incidente>', FormularioIncidentesView.editar_incidentes, name='editarIncidente'),
    path('actualizarIncidente/<int:id_incidente>', FormularioIncidentesView.actualizar_incidentes, name='actualizarIncidente'),
    path('eliminarIncidente/<int:id_incidente>', FormularioIncidentesView.eliminar_incidentes,
         name='eliminarIncidente'),

]
