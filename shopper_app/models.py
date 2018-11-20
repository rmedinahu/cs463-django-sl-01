from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=128)
	price = models.IntegerField()
	description = models.TextField()
	image_url = models.URLField(null=True)


class ShoppingList(models.Model):
	title = models.CharField(max_length=128)


class ShoppingListItem(models.Model):
	shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='shopping_items')
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='shopping_lists')






