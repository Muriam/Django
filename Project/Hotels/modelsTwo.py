from django.db import models


class SalesRecord(models.Model):
    period_code = models.CharField(max_length=10, verbose_name="Код периода") 
    record_code = models.PositiveIntegerField(verbose_name="Код записи") 
    concept = models.CharField(max_length=100, verbose_name="Концепция") 
    dish = models.CharField(max_length=100, verbose_name="Блюдо") 
    dish_category = models.CharField(max_length=100, verbose_name="Категория блюда") 
    dish_quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Количество блюд")
    avg_price_no_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Средняя цена без скидки")
    cost = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Себестоимость")
    discount_sum = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Сумма скидки")
    sum_with_discount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Сумма со скидкой")
    
    class Meta:
        verbose_name = "Запись о продаже"
        verbose_name_plural = "Записи о продажах"
        ordering = ['period_code', 'record_code']

    def __str__(self):
        return f"{self.period_code} | {self.concept} | {self.dish} ({self.dish_quantity})"
