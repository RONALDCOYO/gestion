from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Intervinientes, Productos, Sucursal, Roles, Pedido, Cliente
from .forms import (IntervinienteForm, ProductoForm, SucursalForm, 
                    RolForm, RegistrationForm, PedidoForm, ClienteForm)
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia esto a la página a la que deseas redirigir después del inicio de sesión
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

#Codigo nuevo
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

#Vista para pedidos

class PedidoListView(ListView):
    model = Pedido
    template_name = 'administracion/pedido_list.html'
    context_object_name = 'pedidos'

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'administracion/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'administracion/pedido_form.html'
    success_url = reverse_lazy('pedido_list')
    
class ClienteListView(ListView):
    model = Cliente
    template_name = 'administracion/clientes_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'administracion/cliente_form.html'
    success_url = reverse_lazy('clientes_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'administracion/cliente_form.html'
    success_url = reverse_lazy('clientes_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'administracion/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes_list')    