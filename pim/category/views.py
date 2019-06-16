from django.shortcuts import render
from rest_framework import generics;
from category.models import Category as cg,Product as pd;
from category.serializers import CategorySerializer;
class CategoryListApiView(generics.ListAPIView):
    serializer_class=CategorySerializer;
    model=cg;
    def get_queryset(self):
        queryset=[];
        root=[i for i in cg.objects.filter(root__isnull=True)]
        sub=[i for i in cg.objects.filter(root__isnull=False)];
        for i in root:
            queryset.append(i);
            for j in sub:
                if j.root==i:
                    queryset.append(j)
        return queryset;
