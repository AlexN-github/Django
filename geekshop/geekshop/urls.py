"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from geekshop import settings
from mainapp import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    #path('products/', views.products, name='products'),
    #path('products/all/', views.products_all, name='products_all'),
    #path('products/home/', views.products_home, name='products_home'),
    #path('products/office/', views.products_office, name='products_office'),
    #path('products/modern/', views.products_modern, name='products_modern'),
    #path('products/classic/', views.products_classic, name='products_classic'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

















