from django.shortcuts import render

# Create your views here.
from mainapp.models import Product


def main(request):
    products_list = Product.objects.all()[:4]
    content = {
        'title' : {'name' : "Главная"},
        'products': products_list
    }
    return render(request, 'index.html', content)

def contact(request):
    content = { 'title' : {'name' : "Контакты"}}
    return render(request, 'contact.html', content)

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]
content = {'title': {'name': "Продукты"},
           'links_menu' : links_menu,
          }
def products(request):
    return render(request, 'products.html', content)

def products_all(request):
    #content = { 'title' : {'name' : "Продукты"}}
    return render(request, 'products.html', content)

def products_home(request):
    #content = { 'title' : {'name' : "Продукты"}}
    return render(request, 'products.html', content)

def products_office(request):
    #content = { 'title' : {'name' : "Продукты"}}
    return render(request, 'products.html', content)

def products_modern(request):
    #content = { 'title' : {'name' : "Продукты"}}
    return render(request, 'products.html', content)

def products_classic(request):
    #content = { 'title' : {'name' : "Продукты"}}
    return render(request, 'products.html', content)

