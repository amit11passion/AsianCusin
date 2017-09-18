
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Menu,Menuitem

class IndexView(generic.ListView):
    template_name = 'indiancousin/index.html'
    context_object_name = 'all_menu'

    def get_queryset(self):
        return Menu.objects.all()

class DetailView(generic.DetailView):
    model = Menu
    template_name = 'indiancousin/details.html'


