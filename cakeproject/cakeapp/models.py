from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('birthday', 'birthday'),
        ('variety', 'variety'),
        ('wedding', 'wedding'),
        ('cupcake', 'cupcake'),
        
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def total_price(self):
        return self.product.price * self.quantity
