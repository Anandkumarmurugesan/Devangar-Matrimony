"""Matrimony URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from matrimony_pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.Welcome_page,name='Welcome_page'),
    url(r'Mainpage/',views.Main_page,name='Main_page'),
    url(r'form/',views.form_view,name='form_view'),
    url(r"signup/", views.Sign_up_request, name="register"),
    url(r"login/", views.login_request, name="login"),
    path(r'profile/<str:pk>/',views.profile_page,name='profile'),
    url(r'logout/',views.logout_request,name='logout'),
    url(r'reg/',views.profile_reg_user,name='reg'),
    path(r'update/<str:pk>/',views.form_update,name='update'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
