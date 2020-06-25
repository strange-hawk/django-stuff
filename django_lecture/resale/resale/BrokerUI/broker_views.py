from django.shortcuts import render
from BrokerUI.models import Broker
from BrokerUI.forms import BrokerForm
from SellerUI.views import index


# Create your views here.
def brokerrequest(request):
    form = BrokerForm()
    if request.method=='post' or request.method == 'POST':
        form = BrokerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('form is invalid')

    return render(request,'broker.html',{'form':form})

def broker_list(request):
    listr = Broker.objects.order_by('firstname','lastname')
    data_dictionary = {'data_dict' : listr}
    return render(request,'broker_list.html',context=data_dictionary)

