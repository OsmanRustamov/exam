from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Order, User
from .forms import OrderForm, OrderStatusForm

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('main')

def logout_view(request):
    logout(request)
    return redirect('login')

def main(request):
    order = Order.objects.all()
    user = User.objects.all()
    return render(request, 'main.html', {"orders": order, "user": user})

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("main")
    else:
        form = OrderForm
    return render(request, "add_order.html", {"form": form})


def update_order_status(request, order_id):
    order = get_object_or_404(order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('main')
    return render(request, 'update_order_status.html', {'order': order})


@login_required(login_url='/accounts/login/')
def main(request):
    orders = Order.objects.all()
    return render(request, 'main.html', {'orders': orders})

@login_required(login_url='/accounts/login/')
def order_detail(request, orderid):
    order = get_object_or_404(Order, orderid=orderid)
    return render(request, 'order_detail.html', {'order': order})
from django.contrib.auth.views import LoginView, LogoutView
@login_required(login_url='/accounts/login/')
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def order_update(request, orderid):
    order = get_object_or_404(Order, orderid=orderid)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def order_delete(request, orderid):
    order = get_object_or_404(Order, orderid=orderid)
    if request.method == 'POST':
        order.delete()
        return redirect('main')
    return render(request, 'order_confirm_delete.html', {'order': order})

@login_required(login_url='/accounts/login/')
def order_status_update(request, orderid):
    order = get_object_or_404(Order, orderid=orderid)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('main', orderid=order.orderid)
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'update_order_status.html', {'form': form, 'order': order})
