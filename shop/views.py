from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "shop/product_create.html"
    form_class = ProductCreateForm
    success_url = reverse_lazy("users:dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "shop/product_update.html"
    success_url = reverse_lazy("users:dashboard")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("users:dashboard")
    template_name = "shop/product_delete.html"
