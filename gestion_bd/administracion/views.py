from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Intervinientes, Productos, Sucursal, Roles
from .forms import IntervinienteForm, ProductoForm, SucursalForm, RolForm

def home(request):
    return render(request, 'home.html')

# Gestión de Intervinientes
class IntervinientesView(ListView):
    model = Intervinientes
    template_name = 'administracion/intervinientes_list.html'
    context_object_name = 'intervinientes'

class IntervinienteCreateView(CreateView):
    model = Intervinientes
    form_class = IntervinienteForm
    template_name = 'administracion/interviniente_form.html'
    success_url = reverse_lazy('intervinientes_list')

class IntervinienteUpdateView(UpdateView):
    model = Intervinientes
    form_class = IntervinienteForm
    template_name = 'administracion/interviniente_form.html'
    success_url = reverse_lazy('intervinientes_list')

class IntervinienteDeleteView(DeleteView):
    model = Intervinientes
    template_name = 'administracion/interviniente_confirm_delete.html'
    success_url = reverse_lazy('intervinientes_list')

# Gestión de Productos
class ProductoListView(ListView):
    model = Productos
    template_name = 'administracion/producto_list.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'administracion/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'administracion/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = 'administracion/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

# Gestión de Sucursales
class SucursalListView(ListView):
    model = Sucursal
    template_name = 'administracion/sucursal_list.html'
    context_object_name = 'sucursales'

class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'administracion/sucursal_form.html'
    success_url = reverse_lazy('sucursal_list')

class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'administracion/sucursal_form.html'
    success_url = reverse_lazy('sucursal_list')

class SucursalDeleteView(DeleteView):
    model = Sucursal
    template_name = 'administracion/sucursal_confirm_delete.html'
    success_url = reverse

# Gestión de Roles

class RolListView(ListView):
    model = Roles
    template_name = 'administracion/rol_list.html'
    context_object_name = 'roles'

class RolCreateView(CreateView):
    model = Roles
    form_class = RolForm
    template_name = 'administracion/rol_form.html'
    success_url = reverse_lazy('rol_list')

class RolUpdateView(UpdateView):
    model = Roles
    form_class = RolForm
    template_name = 'administracion/rol_form.html'
    success_url = reverse_lazy('rol_list')

class RolDeleteView(DeleteView):
    model = Roles
    template_name = 'administracion/rol_confirm_delete.html'
    success_url = reverse_lazy('rol_list')
