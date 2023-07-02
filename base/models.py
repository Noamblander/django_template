from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    def __str__(self):
           return self.desc
    

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    amount = models.IntegerField()
    createdTime=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.price = self.price * self.amount
        super(Order, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
           return f'{self.desc}  '
