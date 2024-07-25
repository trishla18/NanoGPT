"""eguru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from adminpanel.views import adminPage
from login.views import loginPage, login
from chat.views import chatPage, ask
from subjects.views import subjectsPage
from topics.views import topicsPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", loginPage, name='login'),
    path("login/", loginPage, name='login3'),
    path("signin/", login, name='signin'),
    path("subjects/", subjectsPage, name='subjects'),
    path("topics/", topicsPage, name='topics'),
    path("chat/", chatPage, name='chatPage'),
    path("ask/", ask, name='ask')
]
