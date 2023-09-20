from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
<<<<<<< HEAD
from django.shortcuts import redirect
=======

>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
from apps.usuario.form import registroform
from django.contrib.auth.models import User

class registrarusuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = registroform
    success_url = reverse_lazy('venta_listar')

    def form_valid(self, form):
        # Antes de guardar el formulario, establece el nombre de usuario en la sesión
        self.request.session['username'] = self.request.user.username
        return super().form_valid(form)
<<<<<<< HEAD

=======
>>>>>>> b0ee205593e0976a99ff5a8437a349abae8f006b
