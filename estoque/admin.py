from django.contrib import admin
from .models import Produto, Categoria, Movimentacao

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nome', 'categoria', 'preco', 'estoque')
    search_fields = ('sku', 'nome', 'categoria')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display   = ('produto','tipo','quantidade','data')
    list_filter    = ('tipo','data','produto')
    readonly_fields= ('data',)
