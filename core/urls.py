"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from django.contrib.auth import views as dj_auth_views

from views import views, example_views, chatgpt_views, user_views
from django.conf.urls import include
from django.contrib import admin
from transcription.views import transcribe

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 模板範例檔
    # view.py
    path('', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('forget/', views.forget),

    path('user/', user_views.user),
    path('user/edit/', user_views.uedit),

    path('theme/', example_views.theme),  # 學習主選單
    path('pic/', example_views.pic),  # 主題圖片
    path('reading/', example_views.reading),  # 開始描述

    path('gtp_reading/', example_views.gtp_reading),
    path('score/', example_views.score),
    path('vocabulary/', example_views.vocabulary),

    path('record/', example_views.record), #錯題本
    path('record_single/', example_views.record_single), #錯題本

    # example_views.py
    path('example/about/', example_views.about),
    path('example/course/', example_views.course),
    path('example/instructor/', example_views.instructor),
    path('example/blog/', example_views.blog),
    path('example/contact/', example_views.contact),
    path('example/theme/', example_views.theme),
    path('example/pic/', example_views.pic),
    path('example/reading/', example_views.reading),
    path('example/gtp_reading/', example_views.gtp_reading),
    path('example/score/', example_views.score),
    path('example/vocabulary/', example_views.vocabulary),
    path('example/record/', example_views.record),
    path('example/record_single/', example_views.record_single),

    path('transcribe/', transcribe),

    # 純網址可連到的頁面(沒放到html)
    path('example/blog/single/', example_views.blog_single),
    path('example/instructor/details/', example_views.instructor_details),

    # chatGPT 串接測試畫面
    path('example/chatbot/', chatgpt_views.chatbot),
]
