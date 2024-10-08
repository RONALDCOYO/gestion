from django import views
from django.contrib import admin
from django.urls import path
from administracion import views as administracion_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', administracion_views.home, name='home'),
    path('login/', administracion_views.login_view, name='login'),
    path('register/', administracion_views.register_view, name='register'),
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
    path('gestion/pedidos/', administracion_views.PedidoListView.as_view(), name='pedido_list'),
    path('gestion/pedidos/create/', administracion_views.PedidoCreateView.as_view(), name='pedido_create'),
    path('gestion/pedidos/<int:pk>/edit/', administracion_views.PedidoUpdateView.as_view(), name='pedido_edit'),
    path('gestion/pedidos/<int:pk>/delete/', administracion_views.PedidoDeleteView.as_view(), name='pedido_delete'),
    #Abonos
    path('gestion/pedidos/<int:pk>/abono/', administracion_views.realizar_abono, name='realizar_abono'),
    #Clientes
    path('gestion/clientes/', administracion_views.ClienteListView.as_view(), name='clientes_list'),
    path('gestion/clientes/create/', administracion_views.ClienteCreateView.as_view(), name='cliente_create'),
    path('gestion/clientes/<int:pk>/edit/', administracion_views.ClienteUpdateView.as_view(), name='cliente_edit'),
    path('gestion/clientes/<int:pk>/delete/', administracion_views.ClienteDeleteView.as_view(), name='cliente_delete'),
    #Rutas para reportes
    path('gestion/reporte-pedidos/', administracion_views.reporte_pedidos, name='reporte_pedidos'),
    path('gestion/reporte-pedidos-pdf/', administracion_views.generar_reporte_pdf, name='reporte_pedidos_pdf'),
    
]
