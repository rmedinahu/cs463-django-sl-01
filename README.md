# cs463-django-sl-01

In this exercise you will become familiar with the major components of a VERY simple web application built with the Django web application framework. Begin with the tasks below.

## Tasks
1. fork this project to your github account

2. clone this project to a directory on your machine and cd into the project directory
create a virtual environment for the django project. This project requires django version 2+ so make sure your virtual environment is constructed with python 3.

3. with your virtual environment activated install the requirements ```pip install -r requirements.txt```

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



