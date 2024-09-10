from django import forms
from .models import Intervinientes, Productos, Sucursal, Roles

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
