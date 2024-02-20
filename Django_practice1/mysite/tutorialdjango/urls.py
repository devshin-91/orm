"""
URL configuration for tutorialdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import (
    index, 
    about,  
    notice, 
    user,
    # notice_1, notice_2, notice_3, 
    # contact, 
    # atod,
    # user_hojun, user_mini,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("about/", about),
    path("notice/<int:pk>", notice),
    path("user/<str:s>/", user),
    # path("notice/1/", notice_1),
    # path("notice/2/", notice_2),
    # path("notice/3/", notice_3),
    # path("contact/", contact),
    # path("a/b/c/d/", atod),
    # path("user/hojun/", user_hojun),
    # path("user/mini/", user_mini),
]
