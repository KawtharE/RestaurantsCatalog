# Restaurants Catalog Simple App

A Flask example that represents the fundamental usage of ORM (SQLAlchemy) and the basic CRUD operations using Python 3.5 

![Starting Screen](https://github.com/KawtharE/RestaurantsCatalog/blob/master/assets/Screencast_2018-03-17_18_30_50.gif)

This kind of applications is better developed by following the **Iterative development process**, which help us, as developers to write code in **Agil way**.

Before starting the first iteration of the process of developing this application, we need to set up the local working enivronment.

## Set up Local development environment

1- Download Python3.5:
    if the machine is Ubuntu or Mac then Python3.5 is already installed.
    if the machine is window, Python3.5 or any other version can be downloaded from [this link](https://www.python.org/downloads/).
    
2- Download Flask0.10:
    [Flask installation](http://flask.pocoo.org/docs/0.10/installation/) documentation.
    
3- Download SQLAlchemy:
    $sudo easy_install sqlalchemy flask-sqlalchemy
    or
    $sudo pip3 install sqlalchemy flask-sqlalchemy
    
## Iteration 1
-Create Mock-ups for every page in the application and design URLs for each one also.
**Pages URLs:**
  -'/restaurants/' and '/': *Read* all restaurants.
  -'/restaurants/<int:restaurant_id>/menu/' and '/restaurants/<int:restaurant_id>/': *Read* one restaurant menu.
  -'/restaurants/newRestaurant/': *Create* a new restaurant.
  -'/restaurants/<int:restaurant_id>/edit/': *Update* the informations of one restaurant.
  -'/restaurants/<int:restaurant_id>/delete/': *Delete* one restaurant.
  -'/restaurants/<int:restaurant_id>/menu/newItem/': *Create* a new item.
  -'/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/': *Update* the informations of one item.
  -'/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/': *Delete* one item from the restaurant menu.
  
## Iteration 2
-Add Routes in the main file (project.py)
for each URL previously designed we nedd to code a route that call a function to be executed:
    
    @app.route('/')
    @app.route('/restaurants/')
    def showAllRestaurants():
        return "Display all restaurants"
    @app.route('/restaurants/newRestaurant/')
    def addNewRestaurant():
        return "Display a form to create new restaurant"
    @app.route('/restaurants/<int:restaurant_id>/')
    @app.route('/restaurants/<int:restaurant_id>/menu/')
    def showRestaurant(restaurant_id):
        return "Display one restaurant"
    @app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
    def editRestaurant(restaurant_id):
        return "Display a form to update one restaurant"
    @app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
    def deleteRestaurant(restaurant_id):
        return "Display a confirmation request for deleting action"
    @app.route('/restaurants/<int:restaurant_id>/menu/newItem/', methods=['GET', 'POST'])
    def addNewItem(restaurant_id):
        return "Display a form to create new item"
    @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
    def editMenuItem(restaurant_id, menu_id):
        return "Display a form to update one item"
    @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
    def deleteMenuItem(restaurant_id, menu_id):
        return "Display a confirmation request for the delete action"
        
## Iteration 3
-Adding Templates: first we need to create a **templates** folder, since flask will by default recognize and search for templates in this folder.

    $mkdir templates
    
Now inside this folder, we need to create eight html files, for each page we need a template:
1-restaurants.html
2-newRestaurant.html
3-editRestaurant.html
4-deleteRestaurant.html
5-menu.html
6-newMenuItem.html
7-editMenuItem.html
8-deleteMenuItem.html

## Iteration 4
**Setup a Database.**
For this step, we need to create new file *database_setup.py* that will contain four part:
          -Configuration: which is the section concerning importing all the necessary modules. 
          -Class code: which we use to represent our data in python.  
          -Table: which represents the specific table in our database. 
          -Mapper: which connect the columns of our table to the class that represent it.
          
          import sys
          from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
          from sqlalchemy.ext.declarative import declarative_base
          from sqlalchemy.orm import relationship

          Base = declarative_base()

          class Restaurant(Base):
            __tablename__ = 'restaurant'

            id = Column(Integer, primary_key=True)
            name = Column(String(250), nullable=False)


          class MenuItem(Base):
            __tablename__ = 'menu_item'

            id = Column(Integer, primary_key=True)
            name = Column(String(250), nullable=False)
            description = Column(String(250))
            categorie = Column(String(250))
            price = Column(String(25), nullable=False)
            restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
            restaurant = relationship(Restaurant)

          engine = create_engine('sqlite:///restaurants.db')
          Base.metadata.create_all(engine)
          
=> The database that we create here is SQLite database with the name restaurants.db and that will be generated after executing the following command:
        
          $python3 database_setup.py
          
## Iteration 5
Now, its time to add CRUD functionality to our application.
At this stage we are going to replace all those return messages to render templates and execute some CRUD functions.



