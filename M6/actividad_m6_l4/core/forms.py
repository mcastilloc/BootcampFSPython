from django import forms
from .models import ConsultaContacto

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre"
    )
    email = forms.EmailField(
        label="Correo electrónico"
    )
    mensaje = forms.CharField(
        widget=forms.Textarea,
        label="Mensaje"
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) < 3:
            raise forms.ValidationError(
                "El nombre debe tener al menos 3 caracteres"
            )
        return nombre

class ConsultaContactoForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ['nombre', 'email', 'mensaje']
