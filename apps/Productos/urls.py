# from django.conf.urls import url, include
<<<<<<< HEAD
from django.urls import include, re_path, path
from apps.Productos.views import  index, ProductosCreate , ProductosList, ProductosEdit, ProductosDelete, ProductosInactivar
=======
from django.urls import include, re_path
from apps.Productos.views import  index, ProductosCreate , ProductosList, ProductosEdit, ProductosDelete
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b


urlpatterns = [
    re_path(r'$', index, name='index'),
    re_path(r'^listar', ProductosList.as_view(), name='Productos_listar'),
    re_path(r'^nuevo$', ProductosCreate.as_view(), name='Productos_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', ProductosEdit.as_view(), name='Productos_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', ProductosDelete.as_view(), name='Productos_eliminar'),
<<<<<<< HEAD
    path(r'inactivar/<int:id>', ProductosInactivar, name='Productos_inactivar'),
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
]
