from django.contrib import admin
from .models import Servicos
from .models import Atendentes
from .models import Resolvedores
from .models import Inserir
from .models import Modificar
from .models import Excluir

@admin.register(Servicos)
class ServicosAdmin (admin.ModelAdmin):
  list_display = ('id', 'servico_completo')

admin.site.register(Resolvedores)

admin.site.register(Atendentes)

@admin.register(Inserir)
class InserirAdmin (admin.ModelAdmin):
  list_display = ('nome', 'telefone','setor', 'data_criação', 'tipo', 'area', 'categoria_n0', 'categoria_n1', 'categoria_n2', 'categoria_n3')
  list_filter = ('setor', 'tipo', 'area', 'categoria_n0')
  search_fields = ('nome', 'telefone','setor', 'data_criação', 'tipo', 'area', 'categoria_n0', 'categoria_n1', 'categoria_n2', 'categoria_n3')
@admin.register(Modificar)
class ModificarAdmin (admin.ModelAdmin):
  list_display = ('nome', 'telefone','setor', 'data_criação', 'serviço_atual', 'tipo', 'area', 'categoria_n0', 'categoria_n1', 'categoria_n2', 'categoria_n3')
  list_filter = ('setor', 'tipo', 'area', 'categoria_n0')
  search_fields = ('nome', 'telefone','setor', 'data_criação', 'serviço_atual', 'tipo', 'area', 'categoria_n0', 'categoria_n1', 'categoria_n2', 'categoria_n3')
  
@admin.register(Excluir)
class ExcluirAdmin (admin.ModelAdmin):
  list_display = ('nome', 'telefone','setor', 'data_criação','serviço') 
  list_filter = ('setor',)
  search_fields = ('nome', 'telefone','setor', 'data_criação','serviço')



# Register your models here.
