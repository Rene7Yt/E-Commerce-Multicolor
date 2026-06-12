from django.contrib import admin
from .models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Producto)