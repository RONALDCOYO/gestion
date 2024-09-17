from django.db import models
from django.db.models import Sum

# Modelo Roles
class Roles(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto-incremental
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Roles'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre

# Modelo Sucursal
class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto-incremental
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Sucursal'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre

# Modelo Intervinientes
class Intervinientes(models.Model):
    cedula = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, blank=True)
    mail = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, db_column='Rol_ID')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Intervinientes'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Productos
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'Productos'
        
    def __str__(self):
        return self.nombre    

# Modelo Cliente
class Cliente(models.Model):
    cedula = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        db_table = 'Clientes'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, blank=True)
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField()
    cantidad_semilla = models.IntegerField(null=True, blank=True)  # Verifica que exista este campo
    fecha_germinacion = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)  # Verifica que exista este campo
    lugar = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    numero_lote = models.CharField(max_length=50)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Verifica que este campo también esté bien definido
    remision = models.CharField(max_length=50, null=True, blank=True)

    def calcular_saldo(self):
        total_abonos = self.lista_abonos.aggregate(total=Sum('cantidad_abonada'))['total'] or 0
        return self.valor_pedido - total_abonos

    def __str__(self):
        return f"Pedido {self.numero_lote} - Cliente: {self.cliente}"


# Modelo Abono
class Abono(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='lista_abonos')  # Usamos 'lista_abonos' como related_name
    cantidad_abonada = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_abono = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Abono {self.cantidad_abonada} para pedido {self.pedido.numero_lote}"
