from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["image", "name", "detail", "price"]


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["image", "name", "detail", "price"]
        labels = {
            "name": "نام محصول",
            "detail": "توضیحات محصول",
            "price": "قیمت محصول",
            "image": "تصویر محصول",
        }
