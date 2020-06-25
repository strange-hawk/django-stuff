from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse,reverse_lazy

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'
    # by default return 'school_list' as context dictionaru

class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'
    # by default return 'school' as context dictionary

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'this is ß'
        return context


# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CBV are awesome')


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    # template_name = 'basic_app/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')