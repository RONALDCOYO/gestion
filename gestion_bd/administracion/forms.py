from django import forms
from .models import Intervinientes, Productos, Sucursal, Roles

class IntervinienteForm(forms.ModelForm):
    class Meta:
        model = Intervinientes
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'

class RolForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
