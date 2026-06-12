from django.contrib import admin
from .models import Faq

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'activa')

    list_editable = ('activa',)

    fields = ('pregunta', 'respuesta', 'activa')
# Register your models here.
