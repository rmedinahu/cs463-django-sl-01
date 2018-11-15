from django.contrib import admin

from .models import Item, ShoppingList, ShoppingListItem

admin.site.register(Item)
admin.site.register(ShoppingList)
admin.site.register(ShoppingListItem)