from django.urls import path
from . import views

urlpatterns = [
    # path('buy/<str:plan_name>/', views.buy_plan, name='buy_plan'),
    path('subscribe/int:pk>/', views.subscribe, name='subscription'),
    path('subscribe/', views.subscribe, name='subscription'),
    path("payment/",views.payment,name='payment'),
    path('payment-status', views.payment_status, name='payment-status')
]
