from SellerUI.models import Vehicle
from django import forms

class VehicleForm(forms.ModelForm):
    class Meta():
        model = Vehicle
        fields = '__all__'