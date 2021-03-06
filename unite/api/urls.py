"""unite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'resources', views.ResourceViewSet)

urlpatterns = [
    url(r'^resources/types/(?P<type_id>\w+)/id/(?P<identifier>\w+)/app/(?P<app_id>\w+)/query/$', views.get_app_resources, name='query'),
    url(r'^resources/types/(?P<type_id>\w+)/id/(?P<identifier>\w+)/app/(?P<app_id>\w+)/set/$', views.set_app_resource, name='set_app_resource'),
] + router.urls
