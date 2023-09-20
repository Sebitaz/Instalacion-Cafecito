from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Productos.models import Productos
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


from apps.Productos.forms import Productosform
from apps.Productos.forms import Productos



# Create your views here.
def index(request):
<<<<<<< HEAD
    return render (request, 'venta/index.html')
=======
    return render (request, 'compra/index.html')
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
#     return render(request, 'Productos/Productos_form.html')
# def Productos_views(request):
#     if request.method =='POST':
#         form = Productosform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Productos:Productos_list')
#     else:
#         form=Productosform()
#     return render (request, 'Productos/Productos_form.html',{'form':form})

class ProductosCreate(CreateView):
    model=Productos
    form_class=Productosform
<<<<<<< HEAD
    context_object_name='obj'
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
    template_name='Productos/Productos_form.html'
    success_url=reverse_lazy('Productos_listar')

class ProductosList(ListView):
    model=Productos
<<<<<<< HEAD
    context_object_name='obj'
    template_name='Productos/Productos_list.html'
    paginate_by = 10
=======
    template_name='Productos/Productos_list.html'
    paginate_by = 4
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b

class ProductosEdit(UpdateView):
    model=Productos
    form_class=Productosform
<<<<<<< HEAD
    context_object_name='obj'
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
    template_name='Productos/Productos_form.html'
    success_url=reverse_lazy('Productos_listar')

class ProductosDelete(DeleteView):
    model=Productos
<<<<<<< HEAD
    context_object_name='obj'
    template_name='Productos/Productos_delete.html'
    success_url=reverse_lazy('Productos_listar')

def ProductosInactivar(request, id):
    template_name="Productos/Productos_inactivar.html"
    contexto={}
    prv=Productos.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Producto no existe" + str(id))
    
    if request.method=='GET':
        contexto={'obj': prv}
    
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        return HttpResponse("Producto Inactivado")

    return render(request, template_name, contexto)
=======
    template_name='Productos/Productos_delete.html'
    success_url=reverse_lazy('Productos_listar')
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
