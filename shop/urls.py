from django.urls import path

from . import views


app_name = "shop"

urlpatterns = [
    path("product/list/", views.product_list, name="product_list"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path(
        "product/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "product/update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
]
