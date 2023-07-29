from django.db import models
from PIL import Image


class Product(models.Model):
    name = models.CharField(max_length=250)
    detail = models.TextField()
    price = models.FloatField(default=0.0)
    image = models.ImageField(default="product.jpg", upload_to="images/")

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
