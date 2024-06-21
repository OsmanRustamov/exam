"""
URL configuration for car_service project.

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
from carservice.views import logout_view, main, add_order, order_detail, order_create, order_update, order_delete, order_preparation_status_update, order_payment_status_update
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(authentication_form=AuthenticationForm, redirect_authenticated_user=True), name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_order/', add_order, name="add_order"),
    path('orders/<int:orderid>/', order_detail, name='order_detail'),
    path('orders/new/', order_create, name='order_create'),
    path('orders/<int:orderid>/edit/', order_update, name='order_update'),
    path('orders/<int:orderid>/delete/', order_delete, name='order_delete'),
    path('orders/<int:orderid>/preparation_status/', order_preparation_status_update, name='order_preparation_status_update'),
    path('orders/<int:orderid>/payment_status/', order_payment_status_update, name='order_payment_status_update'),
    path('', main, name='main'),
]
