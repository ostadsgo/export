from django.urls import path

from . import views


app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("add_product/", views.ProductCreateView.as_view(), name="add_product"),
]
