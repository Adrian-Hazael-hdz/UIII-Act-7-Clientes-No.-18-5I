from django.db import models


class ClienteCRM(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    empresa = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField()
    industria = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    estado_cliente = models.CharField(max_length=50)
    fuente_lead = models.CharField(max_length=50)
    notas_cliente = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class ContactoCRM(models.Model):
    cliente = models.ForeignKey(ClienteCRM, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=100)
    apellido_contacto = models.CharField(max_length=100)
    email_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    cargo_contacto = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_contacto} {self.apellido_contacto}"


class EmpleadoComercial(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    cargo_comercial = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cuota_ventas = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class OportunidadVenta(models.Model):
    cliente = models.ForeignKey(ClienteCRM, on_delete=models.CASCADE)
    nombre_oportunidad = models.CharField(max_length=255)
    descripcion = models.TextField()
    valor_estimado = models.DecimalField(max_digits=15, decimal_places=2)
    etapa_venta = models.CharField(max_length=50)
    fecha_cierre_estimada = models.DateField()
    comercial_responsable = models.ForeignKey(EmpleadoComercial, on_delete=models.CASCADE)
    probabilidad_cierre = models.DecimalField(max_digits=3, decimal_places=2)
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return self.nombre_oportunidad


class ActividadCRM(models.Model):
    oportunidad = models.ForeignKey(OportunidadVenta, on_delete=models.CASCADE)
    contacto = models.ForeignKey(ContactoCRM, on_delete=models.CASCADE)
    tipo_actividad = models.CharField(max_length=50)
    fecha_actividad = models.DateField()
    hora_actividad = models.TimeField()
    descripcion_actividad = models.TextField()
    estado_actividad = models.CharField(max_length=50)
    empleado_realizo = models.ForeignKey(EmpleadoComercial, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_actividad} - {self.fecha_actividad}"


class ProductoServicioCRM(models.Model):
    nombre_item = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_lista = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_item = models.CharField(max_length=50)
    es_recurrente = models.BooleanField()
    fecha_lanzamiento = models.DateField()
    categoria_item = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_item


class DetalleOportunidad(models.Model):
    oportunidad = models.ForeignKey(OportunidadVenta, on_delete=models.CASCADE)
    item = models.ForeignKey(ProductoServicioCRM, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario_acordado = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_item = models.DecimalField(max_digits=10, decimal_places=2)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_agregado = models.DateTimeField()

    def __str__(self):
        return f"Detalle {self.id} de oportunidad {self.oportunidad.id}"
