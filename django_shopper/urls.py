"""django_shopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from shopper_app.views import HomeView, ItemListView, ItemView, ItemCreateView, ShoppingListView, ShoppingListViewAll, ShoppingListCreateView, ShoppingListItemCreateView, ShoppingListDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('item/add/', ItemCreateView.as_view(), name='item_add'),
    path('list/<int:pk>/', ShoppingListView.as_view(), name='shopping_list'),
    path('list/add/', ShoppingListCreateView.as_view(), name='list_add'),
    path('shopping/list/add/', ShoppingListItemCreateView.as_view(), name='list_item_add'),
    path('shopping/list/remove/item/<int:pk>/', ShoppingListDeleteView.as_view(), name='shopping_list_remove_item'),
    path('lists/', ShoppingListViewAll.as_view(), name='shopping_list_all'),
    path('admin/', admin.site.urls),
]
