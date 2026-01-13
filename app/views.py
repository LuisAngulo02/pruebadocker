from django.shortcuts import render
from .models import producto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
class productoList(ListView):
    model = producto
    template_name = "lista.html"
class productoCrear(CreateView):
    model = producto
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy("producto_list")
class productoup(UpdateView):
    model = producto
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('producto_list')
class productodelete(DeleteView):
    model = producto
    template_name = 'delete.html'
    success_url = reverse_lazy('producto_list')


    