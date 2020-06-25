from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from myapp.forms import TestForm,UserForm,EsateForm
from myapp.models import Test,Estate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import authenticate,login


class TestListView(ListView):
    model = Test

class TestCreateView(LoginRequiredMixin,CreateView):
    form_class=TestForm
    login_url = '/login/'
    redirect_field_name = 'myapp/test_form.html'

    model = Test
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # t=form.save(commit=False)
        # print(t)
        print(self.request.user.username)
        print(form.instance.type)
        form.instance.user = User.objects.filter(username=self.request.user.username)[0]
        if (form.instance.type == 'U'):
            form.instance.is_user = True
        if (form.instance.type == 'B'):
            form.instance.is_broker = True
        if (form.instance.type == 'S'):
            form.instance.is_seller = True    
        print(form.instance.is_broker)
        print(form.instance.is_user)
        print(form.instance.is_seller) 
        username = self.request.user.username
        password = self.request.user.password
        print(username,password)
        # t=form.save()
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            messages.error(self.request,message='Profile already created')
            return super().form_invalid(form)

class CreateUserView(CreateView):

    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('new_user')
    form_class = UserForm
    model = User
    def form_valid(self, form):

        form.instance.set_password(form.instance.password)
        valid = super(CreateUserView,self).form_valid(form)
        username,password = form.cleaned_data.get('username'),form.cleaned_data.get('password')
        new_user = authenticate(username=username,password=password)
        login(self.request,new_user)
        return valid

class CreateEstateForm(CreateView):
    template_name = 'myapp/estate_form.html'
    success_url = reverse_lazy('home')
    form_class = EsateForm
    model = Estate

    def form_valid(self,form):
        p=Test.objects.filter(user = self.request.user)[0]
        print(p.user.first_name)
        print(form.instance.price)
        form.instance.broker = p
        print(form.instance.broker.is_broker)
        print(form.instance.broker.user.username)
        if(form.instance.broker.is_broker == False):
            messages.error(self.request,message='Only brokers can register')
            return super().form_invalid(form)
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            return HttpResponse(e.__cause__)

class EstateListView(ListView):
    model = Estate

class EstateDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'myapp/estate_detail.html'
    model = Estate


class EstateUpdateView(UpdateView):
    model = Estate
    fields=['price','bedroom','bathroom']
    template_name = 'myapp/estate_update_form.html'


class BrokerDetailView(DetailView):
    model = Test
    context_object_name = 'test'
    print(Test.pk)
    template_name='myapp/broker_detail.html'

class BrokerUpdateView(UpdateView):
    model = Test
    fields=['phone_number']
    template_name = 'myapp/broker_update.html'