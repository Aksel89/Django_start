from django.shortcuts import render
from mainapp.models import Product


def main (request):
    title = 'Главная'
    products = Product.objects.all()
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def contact (request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', context)


def products (request):
    context = {
        'title': 'каталог'
    }
    return render(request, 'mainapp/products.html', context)

# Create your views here.
