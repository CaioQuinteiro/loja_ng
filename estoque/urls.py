from django.urls import path
from . import views

app_name = 'estoque'
urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='lista'),
    path('novo/', views.ProdutoCreateView.as_view(), name='novo'),
    path('<int:pk>/', views.ProdutoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', views.ProdutoDeleteView.as_view(), name='excluir'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_lista'),
    path('categorias/novo/', views.CategoriaCreateView.as_view(), name='categoria_novo'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categorias/<int:pk>/excluir/', views.CategoriaDeleteView.as_view(), name='categoria_excluir'),
    path('movimentacoes/', views.MovimentacaoListView.as_view(),   name='mov_lista'),
    path('movimentacoes/novo/', views.MovimentacaoCreateView.as_view(), name='mov_novo'),
]