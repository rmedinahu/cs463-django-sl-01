from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(null=True)

    def __str__(self):
        return self.name  # returns a string rep of the object


class ShoppingList(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title  # returns a string rep of the object


class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='shopping_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='shopping_lists')

    def __str__(self):
        return self.item.name + '-' + self.shopping_list.title  # returns a string rep of the object





