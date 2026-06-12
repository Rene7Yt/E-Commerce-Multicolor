"""
URL configuration for multicolor_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importamos las vistas directamente
import marketing.views as marketing_views
import tienda.views as tienda_views

urlpatterns = [
    # 1. El panel de administración
    path('admin/', admin.site.urls),
    
    # 2. La raíz ('') carga el index hermoso de Karol
    path('', marketing_views.inicio, name='inicio'),
    
    # 3. Tu catálogo de la tienda
    path('catalogo/', tienda_views.home, name='home'),
    
    # 4. El resto de tus rutas de la tienda
    path('categoria/<slug:categoria_slug>/', tienda_views.home, name='filtrar_por_categoria'),
    path('carrito/', tienda_views.carrito, name='carrito'),
    path('agregar/<int:producto_id>/', tienda_views.agregar_producto, name='agregar_al_carrito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)