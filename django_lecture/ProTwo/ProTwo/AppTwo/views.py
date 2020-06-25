from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    users_list = User.objects.order_by('first_name','last_name')
    data_dict = {'users_data' : users_list}
    return render(request=request, template_name='index.html',context=data_dict)
