from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=25, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"

class Products(models.Model):
    PRODUCTS = (
        ('Phone', 'Phone'),
        ('Cosmetics', 'Cosmetics'),
        ('Grocery', 'Grocery'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=20, null=True)
    category = models.CharField(max_length=20, null=True, choices=PRODUCTS)
    descreption = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} ${self.price}"

class Order(models.Model):
     STATUS = (
          ('Pending', 'Pending'),
          ('Out For Delivery', 'Out for Delivery'),
          ('Delivered', 'Delivered'),
     )
     customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
     products = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
     date_created = models.DateTimeField(auto_now_add=True, null=True)
     status = models.CharField(max_length=200, choices=STATUS, null=True)
     tags = models.ManyToManyField(Tag)

     def __str__(self):
         return f"The Customer is {self.customer} with the product {self.products} and status of Delivery {self.status} and tags associated with it {self.tags}"