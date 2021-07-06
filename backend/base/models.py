from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Now creating product class
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True) #Not on cascade because if user is no more we don't want the product to be deleted
    name=models.CharField(max_length=200,blank=True,null=True)
    image=models.ImageField(null=True,blank=True)
    brand=models.CharField(max_length=200,blank=True,null=True)
    category=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    rating=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    numReviews=models.IntegerField(null=True,blank=True,default=0)
    price=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    countInStock=models.IntegerField(null=True,blank=True,default=0)
    createdAt=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)#Non editable to avoid conflict

    def __str__(self):
        return self.name

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    rating=models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=7)
    comment=models.TextField(null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    payment_method=models.CharField(max_length=200,null=True,blank=True)
    tax_price=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    shipping_price=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    total_price=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    paid_at=models.DateTimeField(auto_now_add=False,blank=True,null=True)
    is_delivered=models.BooleanField(default=False)
    delivered_at=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.created_at)
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    qty=models.IntegerField(default=0,null=True,blank=True)
    price=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    image=models.CharField(max_length=200,null=True,blank=True)
    _id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    address=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    postal_code=models.CharField(max_length=50,null=True,blank=True)
    shipping_price=models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.address