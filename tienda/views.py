from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Categoria

def home(request, categoria_slug=None):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    categoria_seleccionada = None


    if categoria_slug:

        categoria_seleccionada = Categoria.objects.get(slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categoria_seleccionada)

    context = {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada
    }
    return render(request, 'home.html', context)

def carrito(request):
    return render(request, 'carrito.html')

def agregar_producto(request, producto_id):
    try:
        raise Exception("Error de prueba")
    except:
        messages.error(request, '¡El producto no se ha podido agregar!'    )
    return redirect('home')
