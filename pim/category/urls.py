from category.views import *;
from django.urls import path
from category.views import CategoryListApiView;
urlpatterns = [
    path("categories/",CategoryListApiView.as_view(),name="categories"),
]
