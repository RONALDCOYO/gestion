from django.urls import path
from . import views
from administracion import views
from administracion.views import PedidoListView, PedidoCreateView, PedidoUpdateView
from administracion import views as administracion_views
from .views import (
    IntervinienteListView, IntervinienteCreateView, IntervinienteUpdateView, IntervinienteDeleteView, IntervinientesDeleteView, IntervinientesUpdateView, IntervinientesView,
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    SucursalListView, SucursalCreateView, SucursalUpdateView, SucursalDeleteView,
    RolListView, RolCreateView, RolUpdateView, RolDeleteView
)

urlpatterns = [
    
   


    path('intervinientes/', IntervinientesView.as_view(), name='intervinientes_list'),
    path('intervinientes/<int:pk>/edit/', IntervinientesUpdateView.as_view(), name='intervinientes_edit'),
    path('intervinientes/<int:pk>/delete/', IntervinientesDeleteView.as_view(), name='intervinientes_delete'),

    ##Codigo nuevo
    path('intervinientes/', IntervinienteListView.as_view(), name='interviniente_list'),
    path('cld', IntervinienteCreateView.as_view(), name='interviniente_create'),
    path('intervinientes/<int:pk>/edit/', IntervinienteUpdateView.as_view(), name='interviniente_update'),
    path('intervinientes/<int:pk>/delete/', IntervinienteDeleteView.as_view(), name='interviniente_delete'),
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/new/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/edit/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('sucursales/', SucursalListView.as_view(), name='sucursal_list'),
    path('sucursales/new/', SucursalCreateView.as_view(), name='sucursal_create'),
    path('sucursales/<int:pk>/edit/', SucursalUpdateView.as_view(), name='sucursal_update'),
    path('sucursales/<int:pk>/delete/', SucursalDeleteView.as_view(), name='sucursal_delete'),
    path('roles/', RolListView.as_view(), name='rol_list'),
    path('roles/new/', RolCreateView.as_view(), name='rol_create'),
    path('roles/<int:pk>/edit/', RolUpdateView.as_view(), name='rol_update'),
    path('roles/<int:pk>/delete/', RolDeleteView.as_view(), name='rol_delete'),
    #Rutas para pedidos
    path('gestion/pedidos/', administracion_views.PedidoListView.as_view(), name='pedido_list'),
    
]
