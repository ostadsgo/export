# Generated by Django 4.2.3 on 2023-08-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product.webp', upload_to='images/'),
        ),
    ]
