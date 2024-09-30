from django.db import models


class SalesRanges(models.Model):
    bonus_name = models.CharField(default='Bonus', max_length=40, verbose_name='Defina um nome para esta bonificação')
    active_ranges = models.BooleanField(default=False, verbose_name='Bonificação ativa')
    active_percentage = models.BooleanField(default=False, verbose_name='Definir última faixa como porcentagem')
    def __str__(self) -> str:
        return self.bonus_name

class SaleRange(models.Model):
    sale_range = models.CharField(max_length=40, verbose_name='Faixas')
    value = models.FloatField()
    sales_ranges = models.ForeignKey(SalesRanges, on_delete=models.CASCADE, related_name='sale_range')
    def __str__(self):
        return 'faixa de venda'


    