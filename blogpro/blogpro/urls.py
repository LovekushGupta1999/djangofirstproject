"""
URL configuration for blogpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home1/<int:pk>',views.home1,name='home1'),
    path('about/',views.about,name='about'),
    path('about1/<int:pk>',views.about1,name='about1'),
    path('feature/',views.feature,name='feature'),
    path('feature1/<int:pk>',views.feature1,name='feature1'),
    path('account/',views.account,name='account'),
    path('account1/<int:pk>',views.account1,name='account1'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('register/',views.register,name='register'),
    path('registerdata/',views.registerdata,name='registerdata')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
