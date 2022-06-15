from django.contrib import admin

# Register your models here.
from futbolec.models import Jugador,EquipoF,CampeonatoE,Campeonato

admin.site.register(Jugador)
admin.site.register(EquipoF)
admin.site.register(Campeonato)
admin.site.register(CampeonatoE)
