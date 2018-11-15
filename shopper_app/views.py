from django.shortcuts import render
from django.urls import reverse_lazy

# generic views docs: https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic 

from .models import Item, ShoppingList


class HomeView(generic.TemplateView):
	template_name = 'home.html'


class ItemView(generic.DetailView):
	model = Item
	template_name = 'item.html'
	

class ItemListView(generic.ListView):
	model = Item
	template_name = 'item_list.html'


class ItemCreateView(generic.CreateView):
	model = Item  # Object we want to create
	template_name = 'item_add.html'  # template that displays the form
	# list of attributes we want to display widgets for...
	fields = ['name', 'price', 'description', 'image_url']
	success_url = reverse_lazy('item_list')



# ignore this
class ShoppingListView(generic.DetailView):
	model = ShoppingList
	template_name = 'shopping_list.html'

	def get_context_data(self, **kwargs):
		context = super(ShoppingListView, self).get_context_data(**kwargs)
		sl = self.get_object()
		items = []
		for i in sl.shopping_items.all():
			items.append(i.item)
		context['shopping_list_items'] = items
		return context

