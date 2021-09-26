from django.urls import path
import mainapp.views as mainapp
app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>', mainapp.products, name='category'),
    path('contact/', mainapp.contact, name='contact'),
    path('product/<int:pk>', mainapp.product, name='product'),
    path('product_lists/', mainapp.products_list, name='products_list'),
]
