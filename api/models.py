#from re import M
from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural='category'
        def __str__(self):
            return self.title
class Book(models.Model):
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,related_name='book',on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13)
    pages=models.IntegerField()
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField()
    
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)
    class Meta:
        ordering=['date_created']
    def __str__(self):
        return self.title
class Product(models.Model):
    product_tag=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    price=models.IntegerField()
    stock=models.IntegerField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)
    class Meta:
        ordering=['date_created']
        def __str__(self):
            return self.name
    


    
