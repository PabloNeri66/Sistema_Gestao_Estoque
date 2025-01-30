from django.db import models

# Create your models here.
from django.db import models
from categories.models import Category
from brands.models import Brand


class Product(models.Model):
    title = models.CharField(max_length=500, verbose_name='Nome do Produto')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Categoria')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products', verbose_name='Marca')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    serie_number = models.CharField(max_length=200, null=True, blank=True, verbose_name='Número de Série')
    cost_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name= 'Preço de Custo')
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Preço de Venda')
    quantity = models.IntegerField(default=0, verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title