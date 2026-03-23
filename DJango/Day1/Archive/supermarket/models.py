from django.db import models

# Create your models here.

class Products(models.Model):
    # id = models.AutoField(primary_key=True)
    
    name = models.CharField(unique=True,max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name