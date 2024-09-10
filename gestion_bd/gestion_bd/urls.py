from django.contrib import admin
from django.urls import path
from administracion import views as administracion_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', administracion_views.home, name='home'),
    path('gestion/intervinientes/', administracion_views.IntervinientesView.as_view(), name='intervinientes_list'),
    path('gestion/intervinientes/create/', administracion_views.IntervinienteCreateView.as_view(), name='interviniente_create'),
    path('gestion/intervinientes/<int:pk>/edit/', administracion_views.IntervinienteUpdateView.as_view(), name='interviniente_edit'),
    path('gestion/intervinientes/<int:pk>/delete/', administracion_views.IntervinienteDeleteView.as_view(), name='interviniente_delete'),
    path('gestion/roles/', administracion_views.RolListView.as_view(), name='rol_list'),
    path('gestion/roles/create/', administracion_views.RolCreateView.as_view(), name='rol_create'),
    path('gestion/roles/<int:pk>/edit/', administracion_views.RolUpdateView.as_view(), name='rol_edit'),
    path('gestion/roles/<int:pk>/delete/', administracion_views.RolDeleteView.as_view(), name='rol_delete'),
    path('gestion/productos/', administracion_views.ProductoListView.as_view(), name='producto_list'),
    path('gestion/productos/create/', administracion_views.ProductoCreateView.as_view(), name='producto_create'),
    path('gestion/productos/<int:pk>/edit/', administracion_views.ProductoUpdateView.as_view(), name='producto_edit'),
    path('gestion/productos/<int:pk>/delete/', administracion_views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('gestion/sucursales/', administracion_views.SucursalListView.as_view(), name='sucursal_list'),
    path('gestion/sucursales/create/', administracion_views.SucursalCreateView.as_view(), name='sucursal_create'),
    path('gestion/sucursales/<int:pk>/edit/', administracion_views.SucursalUpdateView.as_view(), name='sucursal_edit'),
    path('gestion/sucursales/<int:pk>/delete/', administracion_views.SucursalDeleteView.as_view(), name='sucursal_delete'),
]
