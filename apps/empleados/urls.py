# from django.conf.urls import url, include
<<<<<<< HEAD
from django.urls import include, re_path, path
from apps.empleados.views import index, empleadosList, EmpleadosUpdate, empleadosCreate, empleadosdelete, EmpleadoInactivar
=======
from django.urls import include, re_path
from apps.empleados.views import index, empleadosList, EmpleadosUpdate, empleadosCreate, empleadosdelete
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
# , EmpleadosUpdate, EmpleadosDelete, EmpleadosUpdate, empleadosdelete

# urlpatterns = [
    #re_path(r'^$', index, name='index'),
    # re_path(r'^listar$', empleados_list, name='empleados_listar'),
    # re_path(r'^nuevo$', empleados_view, name='empleados_crear'),
    #re_path(r'^nuevo$', empleadosCreate.as_view(), name='empleados_crear'),
    #re_path(r'^listar$', empleadosList.as_view(), name='empleados_listar'),
    # re_path(r'^editar/(?P<id_empleados>\d+)/$', EmpleadosUpdate, name='empleados_editar'),
    #re_path(r'^editar/(?P<pk>\d+)/$', EmpleadosUpdate.as_view(), name='empleados_editar'),
    #re_path(r'^eliminar/(?P<pk>\d+)/$', EmpleadosDelete.as_view(), name='empleados_eliminar'),
# ]

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^listar', empleadosList.as_view(), name='empleados_listar'),
    re_path(r'^nuevo$', empleadosCreate.as_view(), name='empleados_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', EmpleadosUpdate.as_view(), name='empleados_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', empleadosdelete.as_view(), name='empleados_eliminar'),
<<<<<<< HEAD
    path(r'inactivar/<int:id>', EmpleadoInactivar, name='empleados_inactivar'),

=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
    # re_path(r'^editar/(?P<id_Empleados>\d+)/$', EmpleadosEdit, name='empleados_editar'),
    # re_path(r'^eliminar/(?P<id_Empleados>\d+)/$', EmpleadosDelete, name='empleados_eliminar'),
]
