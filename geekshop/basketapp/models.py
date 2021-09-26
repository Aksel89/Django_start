from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_date = models.DateTimeField(verbose_name='дата добавления', auto_now=True)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_amount(self):
        _items = Basket.objects.filter(user=self.user)
        _total_amount = sum(list(map(lambda x: x.quantity, _items)))
        return _total_amount

    @property
    def sum_total(self):
        _items = Basket.objects.filter(user=self.user)
        _sum_total = sum(list(map(lambda x: x.product_cost, _items)))
        return _sum_total