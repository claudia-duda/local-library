from django.contrib import admin
from .models import Pessoa


class PessoaList(admin.ModelAdmin):
    list_display=('id', 'nome', 'email')
    list_display_links=('id', 'nome')
    search_fields= ('nome',)

# Register your models here.
admin.site.register(Pessoa,PessoaList)
