from django.db import models

class Roles(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto-incremental
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Roles'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto-incremental
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'Sucursal'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre

class Intervinientes(models.Model):
    cedula = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, blank=True)
    mail = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'Intervinientes'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Productos(models.Model):
    id = models.AutoField(primary_key=True)  # ID auto-incremental
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'Productos'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return self.nombre
