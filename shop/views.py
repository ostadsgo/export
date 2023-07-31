from django.shortcuts import render
from .models import Product
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
    fields = ["image", "name", "detail", "price"]

    template_name = "shop/add_product.html"  # <app>/<model>_<viewtype>.html
    # context_object_name = 'products'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
