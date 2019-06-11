from rest_framework import serializers;
from category.models import Category,Product;
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category;
class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model=Product;