from django.db import models
from category.models import Category
from django.urls import reverse
from src.validators import bleach_validator
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True,validators=[bleach_validator])
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=200,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def color(self):
        return super(VariationManager, self).filter(variation_category='color',is_active=True)
    def size(self):
        return super(VariationManager, self).filter(variation_category='size',is_active=True)
class Variation(models.Model):
    variation_category_choice = (
        ('color','color'),
        ('size','size'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100,choices=variation_category_choice,validators=[bleach_validator])
    variation_value = models.CharField(max_length=100,validators=[bleach_validator])
    is_active = models.BooleanField(default=True)
    created_date= models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value