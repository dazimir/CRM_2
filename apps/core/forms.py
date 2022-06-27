from .models import Customer
from django.forms import ModelForm


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        field = ['first_name', 'last_name', 'email', 'phone']
