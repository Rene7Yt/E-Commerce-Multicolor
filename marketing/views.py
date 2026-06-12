from django.shortcuts import render, redirect
from .models import Faq
from .forms import SugerenciaForm
from django.contrib import messages

def tu_vista_faq(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "¡Tu pregunta fue envida con exito!")
            return redirect('inicio')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, error)
            return redirect('inicio')
    
    return render(request, 'marketing/index.html', {'form': form})

def inicio(request):
    if request.method == 'POST':
        form = SugerenciaForm(request.POST)
        if form.is_valid():
            # Guardamos la pregunta, pero marcada como inactiva para que la aprueben
            nueva_pregunta = form.save(commit=False)
            nueva_pregunta.activa = False
            nueva_pregunta.save()
            messages.success(request, "¡Tu mensaje fue enviado con éxito!")
        else:

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
        
        return redirect('inicio')
    
    # Se extrae solo FAQ que tengan el check de 'activa' en True
    form = SugerenciaForm()
    faqs = Faq.objects.filter(activa=True)
    
    ctx = {
        'faqs': faqs,
        'form': form,
    }

    return render(request, 'marketing/index.html', ctx)