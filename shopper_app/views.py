from django.shortcuts import render

# generic views docs: https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic 

from .models import Item


class HomeView(generic.TemplateView):
	template_name = 'home.html'


class ItemView(generic.DetailView):
	model = Item
	template_name = 'item.html'
	

class ItemListView(generic.ListView):
	model = Item
	template_name = 'item_list.html'


