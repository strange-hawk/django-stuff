from django.shortcuts import render
# from SellerUI.models import User
from SellerUI.forms import VehicleForm
from SellerUI.models import Vehicle

# Create your views here.
def index(request):
    return render(request,'index.html')

def vehiclerequest(request):
    form = VehicleForm()
    if request.method=='post' or request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('form is invalid')

    return render(request,'vehicle.html',{'form':form})

def vehicle_list(request):
    listr = Vehicle.objects.order_by('Vmodel')
    data_dictionary = {'data_dict' : listr}
    return render(request,'vehicle_list.html',context=data_dictionary)
