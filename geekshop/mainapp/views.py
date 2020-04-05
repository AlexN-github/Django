from django.shortcuts import render

# Create your views here.
def main(request):
    content = { 'title' : {'name' : "Главная"}}
    return render(request, 'index.html', content)


def products(request):
    content = { 'title' : {'name' : "Продукты"}}
    return render(request, 'products.html', content)


def contact(request):
    content = { 'title' : {'name' : "Контакты"}}
    return render(request, 'contact.html', content)
