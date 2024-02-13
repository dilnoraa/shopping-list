from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.forms.product_form import ProductForm
from product.models import Product, ShoppingItem
from product.serializers import ShoppingItemSerializer
from django.forms.models import model_to_dict
import json


def product_list_view(request):
    template_path = "product_list.html"
    context_dict = {}
    all_products = Product.objects.all()
    context_dict["data"] = all_products
    return render(request, template_path, context_dict)


def product_view(request, resource_id=None):
    context_dict = {}
    template_path = "product.html"
    if resource_id and request.method == 'GET':
        product = Product.objects.filter(id=resource_id).first()
        product_data = model_to_dict(product) if product else None
        product_form = ProductForm(product_data)
        if product_form.is_valid():
            context_dict["form"] = product_form
            return render(request, template_path, context_dict)
    if request.method == 'DELETE':
        product = Product.objects.get(id=resource_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST' and resource_id:
        product = Product.objects.filter(id=resource_id).first()
        data = request.POST
        product.name = data["name"]
        product.description = data["description"]
        product.category = data["category"]
        product.save()
        messages.success(request, "Created a new product")
        return HttpResponseRedirect("/product_list/")


def products_view(request):
    template_path = "product.html"
    context_dict = {}
    product_form = ProductForm(request.POST or None)
    if request.method == 'GET':
        context_dict["form"] = product_form
        return render(request, template_path, context_dict)
    if request.method == 'POST':
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()
            messages.success(request, "Created a new product")
        return HttpResponseRedirect("/product_list/")


class Shoppinglist(APIView):
    def get(self, request, resource_id=None):
        if resource_id:
            item = ShoppingItem.objects.prefetch_related('product_name').filter(id=resource_id).first()
            serializer = ShoppingItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        items = ShoppingItem.objects.all()
        serializer = ShoppingItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        product_object = Product.objects.filter(name=data["product"]).first()
        item = ShoppingItem()
        item.product_name = product_object
        item.location = data["location"] if data["location"] else ""
        item.price = float(data["price"]) if data["price"] else None
        item.amount = int(data["amount"]) if data["amount"] else 1
        item.save()
        return Response({"id": item.id}, status=status.HTTP_201_CREATED)


def shopping_list_view(request):
    template_path = "shopping_list.html"
    context_dict = {}
    if request.method == 'GET':
        all_items = ShoppingItem.objects.prefetch_related('product_name').all()
        all_products = Product.objects.values_list("name", flat=True)
        context_dict["shopping_items"] = all_items
        context_dict["products"] = all_products
        return render(request, template_path, context_dict)


def main_view(request):
    return render(request, "main.html", {})
