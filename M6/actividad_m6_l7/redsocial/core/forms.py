from django import forms
from .models import ConsultaContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }
