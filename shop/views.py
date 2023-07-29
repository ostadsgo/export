from django.shortcuts import render
from . import models


def product_list(request):
    products = models.Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})
