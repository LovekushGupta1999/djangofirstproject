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
    path('homeadm/<int:pk>',views.homeadm,name='homeadm'),
    path('about/',views.about,name='about'),
    path('about1/<int:pk>',views.about1,name='about1'),
    path('aboutadm/<int:pk>',views.aboutadm,name='aboutadm'),
    path('feature/',views.feature,name='feature'),
    path('feature1/<int:pk>',views.feature1,name='feature1'),
    path('featureadm/<int:pk>',views.featureadm,name='featureadm'),
    path('account/',views.account,name='account'),
    path('account1/<int:pk>',views.account1,name='account1'),
    path('accountadm/<int:pk>',views.accountadm,name='accountadm'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('registerstu/<int:pk>/',views.registerstu,name='registerstu'),
    path('registeradm/',views.registeradm,name='registeradm'),
    path('addtask/<int:pk>', views.addtask, name='addtask'),
    path('addstudentform/<int:pk>', views.addstudentform, name='addstudentform'),
    path('fn11/<int:pk>', views.fn11, name='fn11'),
    path('fn10/<int:pk>', views.fn10, name='fn10'),
    path('allstudent/<int:pk>', views.allstudent, name='allstudent'),
    path('addtaskwindow/<int:pk>', views.addtaskwindow, name='addtaskwindow'),
    path('addtask/<int:pk>', views.addtask, name='addtask'),
    path('showtask/<int:pk>', views.showtask, name='showtask'),
    path('showsol/<int:pk>', views.showsol, name='showsol'),
    path('showtaskuser/<int:pk>', views.showtaskuser, name='showtaskuser'),
    path('solsubmit/<int:pk>/<int:sk>/', views.solsubmit, name='solsubmit'),
    path('showsolstu/<int:pk>/', views.showsolstu, name='showsolstu'),
    path('edit/<int:pk>/<int:it>', views.edit, name='edit'),
    path('edittaskwindow/<int:pk>/<int:it>', views.edittaskwindow, name='edittaskwindow'),
    path('edittask/<int:pk>/<int:it>', views.edittask, name='edittask'),
    path('editstubyadmin/<int:pk>/<int:it>', views.editstubyadmin, name='editstubyadmin'),
    path('editsol/<int:pk>/<int:it>', views.editsol, name='editsol'),
    path('editprofile/<int:pk>/', views.editprofile, name='editprofile'),
    path('editadmprofile/<int:pk>/', views.editadmprofile, name='editadmprofile'),
    path('update/<int:pk>/', views.update, name='update'),
    path('updatestubyadmin/<int:pk>/', views.updatestubyadmin, name='updatestubyadmin'),
    path('updatesol/<int:pk>/', views.updatesol, name='updatesol'),
    path('updateprofile/<int:pk>/', views.updateprofile, name='updateprofile'),
    path('updateadmprofile/<int:pk>/', views.updateadmprofile, name='updateadmprofile'),
    path('deletetask/<int:pk>/<int:it>', views.deletetask, name='deletetask'),
    path('delete/<int:pk>/<int:it>', views.delete, name='delete'),
    path('addfeedback/<int:pk>/<int:it>', views.addfeedback, name='addfeedback'),
    path('deletestubyadmin/<int:pk>/<int:it>', views.deletestubyadmin, name='deletestubyadmin'),
    path('deletesol/<int:pk>/<int:it>', views.deletesol, name='deletesol'),
    path('filterdata/<int:pk>', views.filterdata, name='filterdata'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
