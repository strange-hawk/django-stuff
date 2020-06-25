from django import forms
from BrokerUI.models import Broker

class BrokerForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = Broker
        fields = '__all__'

