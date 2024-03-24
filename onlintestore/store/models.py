from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50, unique=True, validators=[MinLengthValidator(5)]
    )
    description = models.TextField(blank=True, max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Product.objects.get(pk=self.pk)
            if old_instance.quantity != self.quantity:
                HistoryOfChanges.objects.create(
                    product=self,
                    old_quantity=old_instance.quantity,
                    new_quantity=self.quantity,
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class HistoryOfChanges(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_change = models.DateTimeField(auto_now_add=True)
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.date_of_change}: Old Quantity - {self.old_quantity}, New Quantity - {self.new_quantity}"
