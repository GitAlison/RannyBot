from django.contrib import admin
from .models import Pessoa
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome','sobrenome','idade','sexo']
    list_filter = ['sexo']


admin.site.register(Pessoa,PessoaAdmin)

