from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.


class MyModelListView(ListView):
    model = Article
    template_name = 'my_model_list.html'
    context_object_name = 'my_models'


class MyModelCreateView(CreateView):
    model = Article
    template_name = 'my_model_form.html'
    fields = ['name', 'default_language', 'title']
    success_url = reverse_lazy('my_model_list')


class MyModelUpdateView(UpdateView):
    model = Article
    template_name = 'my_model_form.html'
    fields = ['name', 'default_language', 'title']
    success_url = reverse_lazy('my_model_list')