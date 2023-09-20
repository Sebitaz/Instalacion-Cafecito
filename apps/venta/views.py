from django.shortcuts import render
<<<<<<< HEAD
import datetime
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.venta.form import ventaform
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.venta.models import Venta

def index(request):
    return render (request, 'venta/index.html')

<<<<<<< HEAD
class ventacreate(CreateView):
    model= Venta
    form_class= ventaform
    context_object_name='obj'
=======

class ventacreate(CreateView):
    model= Venta
    form_class= ventaform
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
    template_name='venta/venta_form.html'
    success_url=reverse_lazy('venta_listar')
    
class ventalistar(ListView):
    model=Venta
<<<<<<< HEAD
    context_object_name='obj'
    template_name='venta/venta_listar.html'
    # paginate_by=10
=======
    template_name='venta/venta_listar.html'
    paginate_by=2
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b

class ventaeditar(UpdateView):
    model=Venta
    form_class= ventaform
<<<<<<< HEAD
    context_object_name='obj'
=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
    template_name='venta/venta_form.html'
    success_url= reverse_lazy('venta_listar')
    
class ventaborrar(DeleteView):
    model=Venta
<<<<<<< HEAD
    context_object_name='obj'
    template_name='venta/venta_borrar.html'
    success_url= reverse_lazy('venta_listar')

def VentaInactivar(request, id):
    template_name="venta/venta_inactivar.html"
    contexto={}
    prv=Venta.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Venta no existe" + str(id))
    
    if request.method=='GET':
        contexto={'obj': prv}
    
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        return HttpResponse("Venta Inactivado")

    return render(request, template_name, contexto)
=======
    template_name='venta/venta_borrar.html'
    success_url= reverse_lazy('venta_listar')
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
