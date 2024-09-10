from django import forms
from .models import Intervinientes, Productos, Sucursal, Roles
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
