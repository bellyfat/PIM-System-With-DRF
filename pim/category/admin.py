from django.contrib import admin

# Register your models here.
from category.models import Category,Product;
admin.site.register([Category,Product]);