from django.db import models

class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
