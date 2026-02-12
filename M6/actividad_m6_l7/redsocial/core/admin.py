from django.contrib import admin
from .models import Perfil, OfertaTrabajo, ConsultaContacto

# Registrar los modelos para que aparezcan en el admin
admin.site.register(Perfil)
admin.site.register(OfertaTrabajo)
admin.site.register(ConsultaContacto)
