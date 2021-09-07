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
    content = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', content)


def products (request):
    content = {
        'title': 'каталог'
    }
    return render(request, 'mainapp/products.html', content)

# Create your views here.
