from rest_framework import serializers
from .models import Category,Book,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title')
        model=Category
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','category','author','isbn','pages','price','stock','description','status','date_created')
        model=Book
class productSerializers(serializers.ModelSerializer):
    class Meta:
        fields=('id','product_tag','name','category','price','stock','status','date_created')
        model=Product