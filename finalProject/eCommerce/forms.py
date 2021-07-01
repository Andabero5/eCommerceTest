from django import forms
from .models import componente


class componentForm(forms.ModelForm):
    class Meta:
        model = componente
        fields = ["nombre", "imagen", "caracteristica", "precio", "categoria"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

            'caracteristica': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}),
            'categoria': forms.Select(attrs={'class': 'form-select'})
        }
