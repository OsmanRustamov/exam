from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'orderid',
            'carelement',
            'details',
            'liquids',
            'amountdamage',
        )

from django import forms
from .models import Order

class OrderPreparationStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderstatus']
        widgets = {
            'orderstatus': forms.Select(choices=[
                ('готовится', 'Готовится'),
                ('готов', 'Готов')
            ])
        }

class OrderPaymentStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['paymentstatus']
        widgets = {
            'paymentstatus': forms.Select(choices=[
                ('принят', 'Принят'),
                ('оплачен', 'Оплачен')
            ])
        }

