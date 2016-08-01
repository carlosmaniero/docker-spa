"""rest_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from vehicles import views as vehicles_views
from indexer import views as index_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'manufacturers', vehicles_views.ManufacturerViewSet)
router.register(r'vehicles', vehicles_views.VehicleViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/index/filters/', index_views.filters),
    url(r'^api/index/search/', index_views.search),
    url(r'^admin/', admin.site.urls),
]
