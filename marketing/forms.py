from django import forms
from .models import Faq

class SugerenciaForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['pregunta']
        widgets = {
            'pregunta': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe aqui tu duda...'
            }),
        }
    
    def clean_pregunta(self):
        pregunta = self.cleaned_data.get('pregunta')
        if len(pregunta) < 10:
            raise forms.ValidationError("Por favor, escribe una pregunta un poco mas detallada (minimo 10 caracteres).")
        return pregunta