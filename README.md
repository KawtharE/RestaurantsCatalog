# Restaurants Catalog Simple App

A **Flask** example that represents the fundamental usage of **ORM (SQLAlchemy)** and the basic **CRUD operations** using **Python 3.5**. The example is 100% responsive since i have applied the **responsive pattern Flex**. 

![Starting Screen](https://github.com/KawtharE/RestaurantsCatalog/blob/master/assets/Screencast_2018-03-17_18_30_50.gif)

This kind of applications is better developed by following the **Iterative development process**, which help us, as developers to write code in an **Agil way**.

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

Create **Mock-ups** for every page in the application and design URLs for each one also.

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

Add Routes in the main file (project.py) of the project.

for each URL previously designed we nedd to code a route that call a related function to be executed:
    
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
    @app.route('/restaurants/<int:restaurant_id>/edit/')
    def editRestaurant(restaurant_id):
        return "Display a form to update one restaurant"
    @app.route('/restaurants/<int:restaurant_id>/delete/')
    def deleteRestaurant(restaurant_id):
        return "Display a confirmation request for deleting action"
    @app.route('/restaurants/<int:restaurant_id>/menu/newItem/')
    def addNewItem(restaurant_id):
        return "Display a form to create new item"
    @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
    def editMenuItem(restaurant_id, menu_id):
        return "Display a form to update one item"
    @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
    def deleteMenuItem(restaurant_id, menu_id):
        return "Display a confirmation request for the delete action"
        
## Iteration 3

Adding Templates: first we need to create a **templates** folder, since flask will by default recognize and search for templates in this folder.

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

   **-Configuration:** which is the section concerning importing all the necessary modules and creating an instance of *declarative_base* class, this instance will let SQLAlchemy know that our classes correspond tables in our database. 
   
   **-Class code:** which we use to represent our tables as python classes, those classes have to extend the instance class of declarative_base class in order to extend all of its features.  
   
   **-Table:** which represents the specific table in our database. 
   
   **-Mapper:** which connect the columns of our table to the class that represent it.
        
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
          
=> The database that we create here is an **SQLite database** with the name *restaurants.db* and that will be generated after executing the following command:
        
          $python3 database_setup.py
          
## Iteration 5

Now, its time to add CRUD functionalities to our application.

At this stage we are going to replace all those return messages to render templates instead and execute some CRUD functions.

**Note:** The route function in Flask only anwser to **GET** requests by default, but for *Create, Update, and Delete* operations we need to pass **POST** requests, for this reason we need to add in each route function for *Create, Update, and Delete* an new argument to the function which is **methods=['GET', 'POST']**:

      @app.route('/restaurants/newRestaurant/', methods=['GET', 'POST'])
      .
      .
      .
      @app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
      .
      .
      .
      @app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
      .
      .
      .
      @app.route('/restaurants/<int:restaurant_id>/menu/newItem/', methods=['GET', 'POST'])
      .
      .
      .
      @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
      .
      .
      .
      @app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
      .
      .
      .
      
=> Now that the server-app can response to POST requests, we can make forms for creating, updating and deleting restaurants and items.

**Create a new Restaurant:** 

By importing the **request** library from the flask module we can test the method used (POST or GET) using the **request.method** and in case it's POST we can use the **request.form['nameOfTheInputField']** to read the value entred in the form. Now by calling **Restaurant(name=request.form['restaurantName'])** we are creating new instance of the Restaurant class that gonna be saved in restaurant table in our database, next by calling **session.add(..)** we are adding the new instance to database but we still need to call **session.commit()** to add the instance to our database **permanently**. Note that **session** is an instance of **DBSession** wich is an instance of **sessionmaker** which is in fact an interface that SQLAlchemy uses to execute database operations. So in order to make any changes to a database we just need to call a method from the session instance. 

Finally we are using **redirect** method wich is imported from the **flask** module to redirect to the URL we are passing on argument, this argument (the URL) is the result of the execution the function **url_for('methodName', urlArgs)** which is also imported from the flask module and which return the URL that uses the method passed on argument. **url_for** is a good way to generate URLs all around in the application so if we want to change the URL we just change once. 

Now if the request is a **GET** request, we just call **render_template('nameOfTemplate.html', args)** which is also come from the flask module, to render a related template, args are parameters passed from the python code to be used or displayed in HTML file, this called **HTML Escaping** there are two ways to do this either to execute python code in HTML using the keyword **{%...%}** or to display python variables in HTML using the keyword **{{...}}**.  

A good application will inform the user, when an action is successfully executed this will make the user experience much better. For this we gonna import a new method **flash** from **flask** module to display feedbacks whenever an operation is executed with success. First to call this method, we need to imported, then called just after the *session.commit()* function, it takes only the message as parameter: **flash('message to display')**. Next in the HTML file where we want the message to be displayed, we gonna call the function **get_flashed_messages()** which will return an array of messages from the python code to be displayed in the page:

      	{%with messages = get_flashed_messages()%}
				{%if messages%}
					<ul>
					{%for message in messages%}
						<li><strong>&#8277; {{message}}</strong></li>
					{%endfor%}
					</ul>
				{%endif%}
			{%endwith%}

Python code for creating new restaurant:

      @app.route('/restaurants/newRestaurant/', methods=['GET', 'POST'])
      def addNewRestaurant():
         if request.method == 'POST':
            newRestaurant = Restaurant(name=request.form['restaurantName'])
            session.add(newRestaurant)
            session.commit()
            flash('A new restaurant was created successfully, with the name %s'% newRestaurant.name)
            return redirect(url_for('showAllRestaurants'))
         else:
            return render_template('newRestaurant.html')


=> The process is similare for the reste of route.

## Iteration 6

Adding **API endpoints** that can be used with external application. The API request should return a JSON object.

To achieve this iteration, first we need to import **jsonify** from flask and add a **serializable property** to the database setup file then we need to code the route function to return a JSON object.

So in *project.py* file:

      from flask import Flask, request, redirect, url_for, flash, render_template, jsonify
      .
      .
      .
      @app.route('/restaurants/JSON')
      def restaurantsData():
         restaurants = session.query(Restaurant).all()
         return jsonify(restaurants=[restaurant.serialize for restaurant in restaurants])
         
=> This will return all restaurants in JSON file, but still need to add the **serialize** property in *database_setup.py*

      class Restaurant(Base):
         __tablename__ = 'restaurant'

         id = Column(Integer, primary_key=True)
         name = Column(String(250), nullable=False)

         @property
         def serialize(self):
            return {
            'id': self.id,
            'name': self.name
            }
            
=> Same for the MenuItem class if we want to return the menu items for each restaurant.

## Iteration 7

Now that all functionalities are working, it's time for last iteration which is for **Styling the app**.

It is a good practice to always think **resposive**, in order to have your application working in all devices. For this purpose i have followed the **Flex** way by adopting the well knowing **Flex pattern**-**Layout Shifter Pattern**.
