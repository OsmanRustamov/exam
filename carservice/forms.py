from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'orderid',
            'orderstatus',
            'paymentstatus',
            'carelement',
            'details',
            'liquids',
            'amountdamage',
        )

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderstatus']
