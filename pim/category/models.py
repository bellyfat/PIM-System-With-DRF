from django.db import models

# Create your models here.

class NumberChilds(models.Manager):
    def get_queryset(self):
        return super(NumberChilds,self).get_queryset().childs.count();
class Category(models.Model):
    #ثءهف)(objects = models.Manager()
    root=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name="childs");
    category_name=models.CharField(max_length=256,);
    
    # get number of child for each instance of category class
    @property
    def child_number(self):
        return self.childs.count();
    
    def __str__(self):
        return self.category_name;
class Product(models.Model):
    under_category=models.ManyToManyField(Category);
    name=models.CharField(max_length=256);
    quantity=models.IntegerField();
    price=models.CharField(max_length=256);
    code=models.CharField(max_length=256);
    def __str__(self):
        return self.name;
    