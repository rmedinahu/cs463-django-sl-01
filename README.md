# cs463-django-sl-01

## Nov 27
Customizing View and Models Part 2

> (re)fork **or** simply clone this repo again.

Once your code is on your machine:

> Create or reinvoke the appropriate virtual environment. Make sure to run ```pip install -r requirements.txt``` in your VE

> Run ```python manage.py migrate``` to create the db tables

> Using the menu bar options, add 8 or more items, 2 shopping lists, and make some associations between the items and the shopping lists.


### 1. Modify ```ItemView.get_context_data``` to create a template variable that holds a list of shopping lists an item is associated with. Use the *related_name* attribute in the ```ShoppingListItem``` model. Display the list in the template ```item.html```

### 2. Modify the ```shopping_list.html``` template to display the items in the list as a grid that is 4 cells wide. Each cell in the grid shows the image of the item, its name, and its price. The items should remain ordered by price in the grid.

[Generic editing docs](https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-editing/) 

[DeleteView docs and example](https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-editing/#deleteview)

### 3. Add a new view to the ```views.py``` file that deletes a shopping list item association (E.g., removes an item from a shopping list). Use the ```DeleteView``` generic. Each association has a unique primary key (pk) in the database. You can use this value to remove associations.

STEPS:

#### 3a. Add a new view to ```views.py```. Use the following snippet to the view to override the success_url to redirect after successful deletion. NOTE: instead of returning to the home page, it should return to the shopping list page from which the item was deleted. See [reverse](https://docs.djangoproject.com/en/2.1/ref/urlresolvers/#reverse) documentation for pointers on sending arguments. 

```python
def get_success_url(self):
    deleted_item = self.get_object()
    return reverse('home')
```

> Ever wonder what generics you can override? See [Classy Based Views](https://ccbv.co.uk/)
    
#### 3b. Set the template_name for the delete view to ```shopping_list_item_confirm_delete.html``` 

#### 3c. Add a new url pattern to ```urls.py``` that invokes the view. Note: A good url pattern might be *shopping/list/remove/item/<int:pk>/*. Give the pattern a name: *'remove_shopping_list_item'*

#### 3d. Use the named url pattern in step 4. 

#### 4. Modify the ```shopping_list.html``` template to modify the remove button to remove each item from the shopping list. Test.


## Nov 20
Customizing Views and Models

> You can modify you existing code from Nov 15 **or** (re)fork **or** simply clone this repo again.

1. Add a "to string" method to each of the **three** models in ```models.py```. This allows to customize how are objects are printed and displayed. See: https://docs.djangoproject.com/en/2.1/ref/models/instances/#other-model-instance-methods

E.g. for the ShoppingList model:

```python
def __str__(self):
    return self.title
```

> Now open the admin panel and view various objects in the shopping list app. You should see more descriptive labels for each object.

2. Add a menu item to the menu bar to allow users to add items to a shopping list. The url pattern name in my repo is: ```list_item_add```

3. Add a menu item to the menu bar to allow users to view all shopping lists in the application. The url pattern name in my repo is: ```shopping_list_all```

4. Modify the ```ShoppingListView.get_context_data()``` method to sort the items by price ascending. 

## Nov 15 
Form Handling v.2 and Customizing Views

This project has been updated to have the cumulative modifications to shopper app as exercised in class. You have two options for today.

a. Fork then clone this repository again (you may need delete your previous fork and your related work). 

b. Alternatively, you can simply clone this repository to separate directory.

1. Add a link to ```item_list.html``` that takes users to the page for adding items (nov 13)

2. Add a link to the item_add form that opens a new tab to https://images.google.com/ so that users can look up an image url when they are creating a new item. Test your modification by adding a few items to the app using the form.

3. From the shopper_app open: ```models.py``` ```views.py``` ```shopping_list.html```. From the django_shopper directory open: ```urls.py```

4. Add a form to create a new Shopping List object (see ```ItemCreateView``` for example).

    a. Create a new template for displaying the form.

    b. Create a view in views.py for displaying the form (use generic.CreateView). Set the template_name attribute to the file you created in the previous step.

    c. Add a url pattern to ```urls.py``` that displays the shopping list form. Add a link to this url to home.html template.

    d. Test that your new url works and add two shopping lists.


5. Add a form to add items to a shopping list. Hint: Create new form for adding ```ShoppingListItem``` objects (see ```models.py```) to the application. Same process:

    a. Create a new template for displaying the form.

    b. Create a view in views.py for displaying the form (use generic.CreateView). Set the template_name attribute to the file you created in the previous step.

    c. Add a url pattern to ```urls.py``` that displays the shopping list item form. Add a link to this url to the shopping list page .

    d. Test that your new url works and add a few items to each of your lists.


## Nov 13
Form Handling v.1

A walkthrough for adding I/O using model based forms to the Shopper App. Necessary files:

* views.py

* urls.py

* (new)item_add.html

## Nov 8
Template Inheritance

Template inheritance (https://docs.djangoproject.com/en/2.1/ref/templates/language/#template-inheritance) supports the reuse of html code:

1) We define a "base" html (or template) file, 

2) We construct any number of html files (or templates) that inherit from (or extend) the base but provide different content.

The base template usually contains the required structure for an html page. Subsequent templates that extend the base provide the content to be inserted in the relevant location on the page.

To create these "locations" we can specify named blocks in the base template that are then "filled out" in the child templates.

A listing of template tags for the Django template engine: https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#built-in-template-tags-and-filters

Overview of the Django template language: https://docs.djangoproject.com/en/2.1/topics/templates/#the-django-template-language

## Tasks
Start where you left off on the Nov 6 in class exercise. If you weren't in class, you begin by forking the repo. It contains the changes made in the last class.

1. Download and place the base.html file (https://github.com/rmedinahu/cs463-django-sl-01/blob/master/shopper_app/templates/base.html) in the shopper_app/templates directory. base.html provides the basic html document structure required for all pages in the app. The base file also includes the bootstrap css framework.

2. Add named block as a child of the body tag in base.html. Name the block content_body and add some default text. Place after the navbar!

{% block content_body %}If you are reading this you may not be correctly using the base.html template. Content here should be specific to the page you are constructing.{% endblock %}

3. Open home.html and remove all text except for the contents of the body tag. At the very top of home.html indicate that the page should extend base.html.

{% extends "base.html" %}

4. Now wrap the remaining content in the page in the named content_body block.

{% block content_body %}
html content here...
{% endblock content_body%}

5. Repeat steps 3 and 4 for the item.html and item_list.html pages.

6. Now open base.html for editing. Add the correct links to the navbar component so that the menu links to home and item inventory.

7. Since we are now utilizing bootstrap, create a two-column grid for the item.html template. Name on the left (size 3) details on the right (size 12)

8. Open models.py in shopper_app. Add a new field (attribute) called image_url to the Item class. This field should be of type URLField. Set the null attribute of the field to True so that an image can be optional.

image_url = models.URLField(null=True)

FYI: See https://docs.djangoproject.com/en/2.1/ref/models/fields/ for a list of field types in django.

9. Now using your admin page, edit your existing items by providing a url to an image for that item. Google might help.

10. Edit item.html so that it displays an item's image using the image_url attribute. Place this image at the top of the right column.

git commit -a -m 'nov8 edits'
git push origin master
## Nov 6
In this exercise you will become familiar with the major components of a VERY simple web application built with the Django web application framework. Begin with the tasks below.

## Tasks
1. fork this project to your github account

2. clone this project to a directory on your machine and cd into the project directory
create a virtual environment for the django project. This project requires django version 2+ so make sure your virtual environment is constructed with python 3.

3. with your virtual environment activated install the requirements:

```pip install -r requirements.txt```

4. Set up the database for Django

```python manage.py migrate```

5. Create an admin account (username: admin, email, password) and remember what you entered!

```python manage.py createsuperuser```

6. Start the Django development server

```python manage.py runserver```

7. Go to http://localhost:8000 to view the home page of the app.

8. Go to http://localhost:8000/admin/ and create one or two Items.

9. Edit the HomeView template so that it identifies the site and what it does. 

10. Edit the ItemView template so that it displays information for an item.

11. Edit the ItemListView template so that it displays all the items (show the name and price for each) in the database.

12. Edit the ItemListView template so that it each item is rendered as a link (e.g., ```<a href="url to item page">item name</a>```)

13. If everything is working, add and commit your changes to the repo and push your changes to github.

```git commit -a -m 'nov6 edits'```

```git push origin master```



