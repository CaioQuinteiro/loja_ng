from django.db import models

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    sku = models.CharField( 'SKU', max_length=20, unique=True, blank=True, null=True, editable=False)
    nome = models.CharField('Nome', max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        verbose_name='Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    descricao = models.CharField('Descricao', max_length=50, blank=True)
    marca = models.CharField('Marca', max_length=50, blank=True)
    tamanho   = models.CharField('Tamanho', max_length=10, blank=True)
    cor       = models.CharField('Cor', max_length=30, blank=True)
    preco_custo = models.DecimalField('Preço de Custo (R$)', max_digits=10, decimal_places=2, default=0)
    preco     = models.DecimalField('Preço (R$)', max_digits=10, decimal_places=2)
    estoque   = models.PositiveIntegerField('Quantidade em estoque', default=0)

    def __str__(self):
        return f"{self.sku} – {self.nome}"
    
    def save(self, *args, **kwargs):
        if not self.sku:
            super().save(*args, **kwargs)
            
            cat_nome = self.categoria.nome if self.categoria else 'XXX'
            cat  = cat_nome[:3].upper()

            cor  = (self.cor or 'XXX')[:3].upper()
            tam  = (self.tamanho or 'U')[:1].upper()
            seq  = str(self.id).zfill(4)

            self.sku = f"{cat}-{cor}-{tam}-{seq}"
            return super().save(update_fields=['sku'])

        super().save(*args, **kwargs)

class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]

    produto   = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='movimentacoes')
    tipo      = models.CharField('Tipo', max_length=1, choices=TIPO_CHOICES)
    quantidade= models.PositiveIntegerField('Quantidade')
    data      = models.DateTimeField('Data e hora', auto_now_add=True)

    class Meta:
        ordering = ['-data']

    def save(self, *args, **kwargs):
        # Se for novo ajuste o estoque do produto
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            if self.tipo == 'E':
                self.produto.estoque += self.quantidade
            else:
                self.produto.estoque = max(self.produto.estoque - self.quantidade, 0)
            self.produto.save(update_fields=['estoque'])
