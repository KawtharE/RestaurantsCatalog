from flask import Flask, request, redirect, url_for, flash, render_template, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def showAllRestaurants():
	restaurants = session.query(Restaurant).all()
	return render_template('restaurants.html', restaurants=restaurants)

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

@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def showRestaurant(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	restaurant_menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
	return render_template('menu.html', restaurant=restaurant, restaurant_menu=restaurant_menu)

@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		newName = request.form['newName']
		restaurant.name = newName
		session.add(restaurant)
		session.commit()
		flash('The restaurant name was changed successfully')
		return redirect(url_for('showAllRestaurants', restaurant_id=restaurant.id))
	else:
		return render_template('editRestaurant.html', restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		session.delete(restaurant)
		session.commit()
		flash('The restaurant was successefully deleted')
		return redirect(url_for('showAllRestaurants'))
	else:
		return render_template('deleteRestaurant.html', restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/menu/newItem/', methods=['GET', 'POST'])
def addNewItem(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		newItem = MenuItem(name=request.form['name'], description=request.form['description'], price=request.form['price'], categorie=request.form['categorie'], restaurant_id=restaurant.id)
		session.add(newItem)
		session.commit()
		flash('A new Item was added To the Menu')
		return redirect(url_for('showRestaurant', restaurant_id=restaurant.id))
	else:
		return render_template('newMenuItem.html', restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menu = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		menu.name = name=request.form['name']
		menu.description = description=request.form['description']
		menu.price = price=request.form['price']
		menu.categorie = categorie=request.form['categorie']
		session.add(menu)
		session.commit()
		return redirect(url_for('showRestaurant', restaurant_id=restaurant.id))
	else:
		return render_template('editMenuItem.html', restaurant=restaurant, menu=menu)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menu = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		session.delete(menu)
		session.commit()
		flash('The Item was deleted successfully')
		return redirect(url_for('showRestaurant', restaurant_id=restaurant.id))
	else:
		return render_template('deleteMenuItem.html', restaurant=restaurant, menu=menu)

@app.route('/restaurants/JSON')
def restaurantsData():
	restaurants = session.query(Restaurant).all()
	return jsonify(restaurants=[restaurant.serialize for restaurant in restaurants])

@app.route('/restaurants/<int:restaurant_id>/JSON')
def restaurantData(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
	return jsonify(restaurant=[item.serialize for item in menu])

if __name__ == "__main__":
	app.secret_key = 'secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)