from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
class product_all(models.Model):
    name =models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_image/')
    category =models.ForeignKey(category,on_delete=models.CASCADE)
    about = models.TextField(max_length=150)
    old_price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    add_date = models.DateField()
    def __str__(self) -> str:
        return self.name