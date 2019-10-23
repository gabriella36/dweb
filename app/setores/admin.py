from django.contrib import admin
from .models import Informatica, Limpeza, Cozinha, Administracao

admin.site.register(Informatica)
admin.site.register(Limpeza)
admin.site.register(Cozinha)
admin.site.register(Administracao)