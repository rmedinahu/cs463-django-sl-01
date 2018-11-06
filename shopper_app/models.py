from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=128)
	price = models.IntegerField()
	description = models.TextField()


