# cs463-django-sl-01
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



