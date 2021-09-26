from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import title
from .models import Product, ProductCategory, Contact
from basketapp.models import Basket
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_similar_products(hot_product):
    similar_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return similar_products


def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    title = 'Контакты'
    contacts = Contact.objects.all()
    content = {
        'title': title,
        'contacts': contacts,
    }
    return render(request, 'mainapp/contact.html', content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            products = Product.objects.filter(category__pk=pk).order_by('price')
            category = get_object_or_404(ProductCategory, pk=pk)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    similar_products = get_similar_products(hot_product)
    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'similar_products': similar_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)


def products_list(request, pk=None):
    basket = []
    links_menu = ProductCategory.objects.all()

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            products = Product.objects.filter(category__pk=pk)
            category = get_object_or_404(ProductCategory, pk=pk)

        content = {
            'title': title,
            'category': category,
            'products': products,
            'links_menu': links_menu,
            'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', content)


def product(request, pk=None):
    title = 'продукт'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', content)
