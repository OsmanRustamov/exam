from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import generics 
from .models import order
from .serializers import OrderSerializer

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('main')

class LogoutView(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('login')

def MainView(request):
    orders = order.objects.all()
    return render(request, "main.html", {"orders": orders})