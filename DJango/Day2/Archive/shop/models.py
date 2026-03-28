from django.db import models

# Create your models here.

gender_choices = [("male", "Male"), ("female", "Female")]

class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_by = models.ForeignKey("MyUser", on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    customer= models.OneToOneField("Customer", on_delete=models.CASCADE, related_name="product_customer", null=True, blank=True)
    image= models.ImageField(upload_to="product_images/", null=True, blank=True)
    def __str__(self):
        return self.name
    
class MyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True, null=True)
    gender= models.CharField(max_length=6, choices=gender_choices)
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at =models.DateTimeField(auto_now_add=True)
    gender= models.CharField(max_length=6, choices=gender_choices)
    def __str__(self):
        return self.name
    

class Product2 (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    created_by = models.ForeignKey("MyUser", on_delete=models.CASCADE, related_name="products2")
    created_at = models.DateTimeField(auto_now_add=True)
    customer= models.ManyToManyField("Customer", related_name="product2_customer", blank=True)
    
    def __str__(self):
        return self.name
    
    
class orders(models.Model):
    product = models.ForeignKey(Product2, on_delete=models.CASCADE, related_name="orders_product")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders_customer")
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Order of {self.product.name} by {self.customer.name}"