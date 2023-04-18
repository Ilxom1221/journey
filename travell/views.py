from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product

# Create your views here.


class ProductList(ListView):
    model = Product
    extra_context = {
        'title': 'IONIZE Главная страница'
    }
    template_name = 'travell/truest.html'