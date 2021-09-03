from django.shortcuts import render


def main (request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


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
