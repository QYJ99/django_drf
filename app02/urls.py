# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 17:10
# @Author  : Cat
# @FileName: urls.py


from django.contrib import admin
from django.urls import path, include
from app02 import views

urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),


]