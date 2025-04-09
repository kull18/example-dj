import firstProject.view as view
from django.contrib.auth.views import LogoutView
from .view import activity_detail, activity_list, create_activity, juego_escribir, count_game  

"""
URL configuration for firstProject project.

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
from django.contrib.auth import views as auth_views  # Corregido



urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", activity_list, name="activity_list"),
    path("juego_escribir", juego_escribir, name="juego_escribir"),
    path('activity/<int:activity_id>/', activity_detail, name='activity_detail'),
        path('create/', create_activity, name='create_activity'),
    path("contar/", count_game, name="count_game"),
]