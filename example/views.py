from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework import generics
from .forms import OrderForm
from .models import order, employee
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
    is_waiter = employee.objects.filter(department="официант").exists()
    is_chef = employee.objects.filter(department="повар").exists()
    return render(request, "main.html", {"orders": orders, "is_waiter": is_waiter, "is_chef": is_chef})

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("main")
    else:
        form = OrderForm
    return render(request, "add_order.html", {"form": form})