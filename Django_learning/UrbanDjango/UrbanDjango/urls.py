"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from second_task.views import *
# from third_task import *
from fourth_task.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_views/', task2nd_view),
    path('class_view/', View2ndTask.as_view),
    path('platform/', shop_view),
    path('platform/cart/', cart_view),
    path('platform/games/', game_view),
    path('platform/registration_view', registration_view)
]
