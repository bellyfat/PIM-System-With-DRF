
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis',include("category.urls")),
    path("rest",include('rest_framework.urls')),
]
