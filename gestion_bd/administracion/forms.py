from django import forms
from django.urls import reverse_lazy
from .models import Abono, Intervinientes, Productos, Sucursal, Roles, Pedido, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class IntervinienteForm(forms.ModelForm):
    class Meta:
        model = Intervinientes
        fields = '__all__'  # Esto incluirá todos los campos del modelo Intervinientes.

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'  # Esto incluirá todos los campos del modelo Productos.

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'  # Esto incluirá todos los campos del modelo Sucursal.

class RolForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'  # Esto incluirá todos los campos del modelo Roles.

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'producto', 'observaciones', 'fecha_pedido', 'cantidad', 'cantidad_semilla',
                  'fecha_germinacion', 'fecha_entrega', 'lugar', 'modelo', 'numero_lote', 'valor_pedido', 'saldo', 'remision']

class AbonoForm(forms.ModelForm):
    class Meta:
        model = Abono
        fields = ['pedido', 'cantidad_abonada']
        
    def __init__(self, *args, **kwargs):
        super(AbonoForm, self).__init__(*args, **kwargs)
        # Cambiamos la etiqueta del campo 'cantidad_abonada'
        self.fields['cantidad_abonada'].label = "Realizar nuevo abono"    


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'direccion', 'telefono', 'email']
        
