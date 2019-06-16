from rest_framework import serializers;
from category.models import Category,Product;

class CategorySerializer(serializers.ModelSerializer):
    """
    used to list all categories with thier nested categories
    """
    class Meta:
        model=Category;
        fields=('root','category_name')
class ProductSerializer(serializers.ModelSerializer):
    """
    used to list all products
    """
    class Meta:
       model=Product;