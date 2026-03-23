from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Products
# Create your views here.

def home(request):
    return render(request, "home.html")

def products(request):
    if request.method == "GET":
        products = Products.objects.all()
        return render(request, "products.html", {"products": products})
    
    elif request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        product = Products.objects.create(name=name, price=price, quantity=quantity)
        products = Products.objects.all()
        return render(request, "products.html", {"products": products,'msg':f"Product {product.name} created successfully!"})
    
def product_delete(request, id):
        product = Products.objects.get(id=id)
        product.delete()
        products = Products.objects.all()
        return redirect("products")