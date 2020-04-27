import datetime
import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp.management.commands.fill_db import load_from_json
from mainapp.models import Product, ProductCategory
from django.db.models import Sum


def main(request):
    title = 'главная'
    products = Product.objects.all()[:3]
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'index.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products



def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)
    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, \
                                              category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, \
                                              is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    #same_products = Product.objects.all()[3:5]
    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'products.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'product.html', content)


def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()

    #locations = load_from_json('contact_locations')

    content = {
        'title': title,
        'visit_date': visit_date,
      #  'locations': locations,
        'basket': get_basket(request.user),
    }
    return render(request, 'contact.html', content)