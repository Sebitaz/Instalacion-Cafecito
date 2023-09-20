<<<<<<< HEAD
from django.urls import include, re_path, path
from apps.cliente.views import client, ClienteEdit, ClienteList, ClienteCreate, ClienteDelete, ClienteUpdate, Clientedelete, ClienteInactivar
=======
from django.urls import include, re_path
from apps.cliente.views import client, ClienteEdit, ClienteList, ClienteCreate, ClienteDelete, ClienteUpdate, Clientedelete
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b

urlpatterns = [
    re_path(r'^$', client, name='client'),
    re_path(r'^listar$', ClienteList.as_view(), name='cliente_listar'),
    re_path(r'^nuevo$', ClienteCreate.as_view(), name='cliente_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', ClienteUpdate.as_view(), name='cliente_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', Clientedelete.as_view(), name='cliente_eliminar'),
    re_path(r'^editar/(?P<id_cliente>\d+)/$', ClienteEdit, name='cliente_editar'),
    re_path(r'^eliminar/(?P<id_cliente>\d+)/$', ClienteDelete, name='cliente_eliminar'),
<<<<<<< HEAD
    path(r'inactivar/<int:id>', ClienteInactivar, name='cliente_inactivar'),
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
]
