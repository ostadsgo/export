from django.urls import path

from . import views


app_name = "shop"

urlpatterns = [
    path("product/list/", views.product_list, name="product_list"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
]
