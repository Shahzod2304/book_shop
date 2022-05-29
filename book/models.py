from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    about = models.CharField(max_length=10000)
    price = models.PositiveIntegerField()
    muallif = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.book_name

class NewsPageModel(models.Model):
    n_title = models.CharField(max_length=300)
    n_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    n_date = models.DateField()
    n_body = models.TextField()
    n_image = models.ImageField(upload_to='images_news/', blank=True)

    def __str__(self):
        return self.n_title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL,null=True,blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField() 

    def __str__(self):
        return "Cart " + str(self.cart.id) + " CartProduct: " + str(self.id)