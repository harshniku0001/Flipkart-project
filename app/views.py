from django.shortcuts import render 
from app.models import main, sub_category, product,category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    cat_list = main.objects.all() 
    return render(request, 'index.html', {'cat_list': cat_list})


def item(request):
    return render(request, 'main/items.html')


def sub_cat(request, id):
    sub = sub_category.objects.filter(cat_id=id)
    return render(request, 'main/sub_cat.html', {"sub": sub})

def product1(request, id):  
    products = product.objects.filter(sub_id=id)
    return render(request, 'main/product1.html', {'products': products})

def detail(request, id):
    product_detail = detail.objects.filter(product, id=id)
    return render(request, 'main/detail.html', {'product': product_detail})
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id', 'main_id', 'name']

class subSerializer(serializers.ModelSerializer):
    class Meta:
        model = sub_category
        fields = ['id', 'cat_id', 'name']



class CategoryList(APIView):
    def get(self, request):
        categories = category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status="200")           




class sub_catList(APIView):
    def get(self, request):
        name = request.query_params.get("name")
        sub = sub_category.objects.filter(name=name)
        serializer = subSerializer(sub, many=True)
        return Response(serializer.data, status="200")           



