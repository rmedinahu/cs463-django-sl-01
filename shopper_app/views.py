from django.shortcuts import render
from django.urls import reverse_lazy

# generic views docs: https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic 

from .models import Item, ShoppingList, ShoppingListItem


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

# Step 4
class ShoppingListCreateView(generic.CreateView):
	model = ShoppingList
	template_name = 'shopping_list_add.html'
	fields = ['title',]
	success_url = reverse_lazy('home')

# Step 5
class ShoppingListItemCreateView(generic.CreateView):
	model = ShoppingListItem
	template_name = 'shopping_list_item_add.html'
	fields = ['shopping_list', 'item']
	success_url = reverse_lazy('home')

class ShoppingListViewAll(generic.ListView):
	model = ShoppingList
	template_name = 'shoppings_list_listall.html'

	
class ShoppingListView(generic.DetailView):
	model = ShoppingList
	template_name = 'shopping_list.html'

	# Method override of DetailView
	def get_context_data(self, **kwargs):
		context = super(ShoppingListView, self).get_context_data(**kwargs)
		sl = self.get_object()
		# create a list of RELATED items to the current shopping list (sl)
		items = []
		# item_obj.price ==> item_obj__price
		for i in sl.shopping_items.all().order_by('item__price'):
			items.append(i.item)
		context['shopping_list_items'] = items
		# print(items)
		return context

