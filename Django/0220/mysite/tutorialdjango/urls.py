from django.contrib import admin
from django.urls import path
from main.views import index, a, b, c, hojun, orm

urlpatterns = [
    path("admin/", admin.site.urls), # path('<경로>', <함수>) => <경로>에 접속했을 때 views.py의 <함수>를 호출해라.
    path("", index),
    path("a/", a),
    path("b/", b),
    path("c/", c),
    path("hojun/", hojun),
    path("orm/", orm),
]