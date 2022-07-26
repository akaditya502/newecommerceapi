from django.shortcuts import render
from .models import Category,Book,Product
from rest_framework import generics
from .serializers import CategorySerializer,BookSerializer,productSerializers

# Create your views here.
class ListCategory(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ListBook(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
class ListProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=productSerializers
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=productSerializers
