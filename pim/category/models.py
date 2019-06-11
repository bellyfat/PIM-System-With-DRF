from django.db import models

# Create your models here.
class Category(models.Model):
    root=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,);
    category_name=models.CharField(max_length=256,);
    def __str__(self):
        return self.category;
class Product(models.Model):
    under_category=models.ManyToManyField(Category,);
    name=models.CharField(max_length=256);
    quantity=models.IntegerField();
    price=models.CharField(max_length=256);
    code=models.CharField(max_length=256);
    def __str__(self):
        return self.name;
    