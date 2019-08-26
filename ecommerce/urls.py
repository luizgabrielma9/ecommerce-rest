"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# REST
from rest_framework import routers

# A partir dos apps
from core.api.viewsets import LojistaViewset, ProdutoViewset, EstoqueViewset

router = routers.DefaultRouter()
router.register(r'lojistas', LojistaViewset, basename='lojista')
router.register(r'produtos', ProdutoViewset, basename='produto')
router.register(r'estoques', EstoqueViewset, basename='estoque')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
