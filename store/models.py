from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    description=models.TextField(max_length=500, blank=True)
    price=models.IntegerField()
    is_available=models.BooleanField(default=True)
    stock=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)


    def get_url(self):
        """returns the url for the product"""
        return reverse('product', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name