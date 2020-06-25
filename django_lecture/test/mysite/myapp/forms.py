from django import forms
from myapp.models import Test,Estate
from django.contrib.auth.models import User
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['type','phone_number']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password' )

class EsateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['bedroom','bathroom','area','price']