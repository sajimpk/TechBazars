from django.db import models
from django.contrib.auth.models import User
from product.models import product_all
# Create your models here.
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_all, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username
    
class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product_all, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username