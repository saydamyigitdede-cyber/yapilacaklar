# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 12:30:01 2025

@author: yigit
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('giris/', views.kullanici_giris, name='giris'),
    #path('kayit/', views.kullanici_kayit, name='kayit'),
    path('cikis/', views.kullanici_cikis, name='cikis'),
]