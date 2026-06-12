from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True) # Esencial para el cliente
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True) # Para subir archivos reales
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True) # Truco pro: para desactivar un producto sin borrarlo

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTATUS_CHOICES = [
        ('PENDIENTE', 'Pendiente por Validar'),
        ('APROBADO', 'Pago Aprobado'),
        ('ENVIADO', 'Enviado'),
        ('CANCELADO', 'Cancelado'),
    ]

    PAGO_CHOICES = [
        ('PAGO_MOVIL', 'Pago Movil'),
        ('ZELLE', 'Zelle'),
        ('BINANCE', 'Binance (USDT)'),
        ('TRANSFERENCIA', 'Transferencia Bancaria'),
    ]

    # Relaciones y datos basicos
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='PENDIENTE')

    # Campos de Envio
    nombre_receptor = models.CharField(max_length=150, default="No especificado")
    telefono = models.CharField(max_length=20, default="No especificado")
    direccion_envio = models.TextField(default="No especificada")

    # Campos de Facturación
    metodo_pago = models.CharField(max_length=20, choices=PAGO_CHOICES, default='PAGO_MOVIL')
    comprobante = models.ImageField(upload_to='comprobantes/', null=True, blank=True)

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username} ({self.get_estatus_display()})"
    

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Orden #{self.pedido.id})"