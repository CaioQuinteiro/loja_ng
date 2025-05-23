from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from django.urls import reverse_lazy
from django.db.models import Sum, F, DecimalField
from .models import (Produto, Categoria, Movimentacao)

# PRODUTO

class ProdutoListView(ListView):
    model = Produto

class ProdutoDetailView(DetailView):
    model = Produto

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome','categoria','marca', 'descricao','tamanho','cor','preco_custo', 'preco','estoque']  
    success_url = reverse_lazy('estoque:lista')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome','categoria','marca', 'descricao','tamanho','cor','preco']
    success_url = reverse_lazy('estoque:lista')

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('estoque:lista')

# CATEGORIA

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'estoque/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'estoque/categoria_form.html'
    success_url = reverse_lazy('estoque:categoria_lista')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'estoque/categoria_form.html'
    success_url = reverse_lazy('estoque:categoria_lista')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'estoque/categoria_confirm_delete.html'
    success_url = reverse_lazy('estoque:categoria_lista')

# MOVIMENTAÇÃO

class MovimentacaoListView(ListView):
    model = Movimentacao
    template_name = 'estoque/movimentacao_list.html'
    context_object_name = 'movs'
    paginate_by = 20

class MovimentacaoCreateView(CreateView):
    model = Movimentacao
    fields = ['produto','tipo','quantidade']
    template_name = 'estoque/movimentacao_form.html'
    success_url = reverse_lazy('estoque:mov_lista')


# DASHBOARD

class DashboardView(TemplateView):
    template_name = 'estoque/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # 1) Total de produtos registrados
        ctx['total_registrados'] = Produto.objects.count()
        # 2) Total de unidades em estoque
        ctx['total_unidades'] = Produto.objects.aggregate(
            total=Sum('estoque')
        )['total'] or 0
        # 3) Valor total gasto (estoque * preco_custo)
        ctx['total_gasto'] = Produto.objects.aggregate(
            gasto=Sum(
                F('estoque') * F('preco_custo'),
                output_field=DecimalField()
            )
        )['gasto'] or 0
        return ctx