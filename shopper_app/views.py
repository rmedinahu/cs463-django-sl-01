from django.shortcuts import render
from django.urls import reverse_lazy, reverse

# generic views docs: https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic 

from .models import Item, ShoppingList, ShoppingListItem


class HomeView(generic.TemplateView):
	template_name = 'home.html'


class ItemView(generic.DetailView):
	model = Item
	template_name = 'item.html'

	def get_context_data(self, **kwargs):
		context = super(ItemView, self).get_context_data(**kwargs)
		return context


class ItemListView(generic.ListView):
	model = Item
	template_name = 'item_list.html'


class ItemCreateView(generic.CreateView):
	model = Item  # Object we want to create
	template_name = 'item_add.html'  # template that displays the form
	# list of attributes we want to display widgets for...
	fields = ['name', 'price', 'description', 'image_url']
	success_url = reverse_lazy('item_list')

	# def get_success_url(self):
	# 	print(self.get_object())
	# 	return reverse_lazy('home')

class ShoppingListCreateView(generic.CreateView):
	model = ShoppingList
	template_name = 'shopping_list_add.html'
	fields = ['title',]
	success_url = reverse_lazy('home')


class ShoppingListItemCreateView(generic.CreateView):
	model = ShoppingListItem
	template_name = 'shopping_list_item_add.html'
	fields = ['shopping_list', 'item']
	success_url = reverse_lazy('home')


class ShoppingListViewAll(generic.ListView):
	model = ShoppingList
	template_name = 'shopping_list_listall.html'

	
class ShoppingListView(generic.DetailView):
	model = ShoppingList
	template_name = 'shopping_list.html'

	# Method override of DetailView
	def get_context_data(self, **kwargs):
		context = super(ShoppingListView, self).get_context_data(**kwargs)
		sl = self.get_object()
		context['shopping_list_items'] = sl.shopping_items.all().order_by('item__price')
		
		return context

