from django.db import models

class Product(models.Model):
    title = models.TextField(max_length=125)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title