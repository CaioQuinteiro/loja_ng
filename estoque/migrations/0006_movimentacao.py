# Generated by Django 5.2.1 on 2025-05-23 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_produto_preco_custo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1, verbose_name='Tipo')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data e hora')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimentacoes', to='estoque.produto')),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
    ]
