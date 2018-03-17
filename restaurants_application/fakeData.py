from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Menu for The Forest Hound
restaurant1 = Restaurant(name="The Forest Hound")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Beef Meat", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$5.25", categorie="Burgers", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="Grilled Sausage", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$6.99", categorie="Hot Dogs", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Black Tea", description="Lorem ipsum dolor sit amet",
                     price="$12.25", categorie="Drinks", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Chocolate Cheesecake", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$5.75", categorie="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Mineral Water", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$5.99", categorie="Drinks", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for The Italian Apple
restaurant2 = Restaurant(name="The Italian Apple")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$7.99", categorie="Burgers", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="Peking Duck", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", price="$25", categorie="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$15", categorie="Hot Dogs", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nepali Momo ", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$12", categorie="Burgers", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Beef Noodle Soup", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$14", categorie="Burgers", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Ramen", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$12", categorie="Hot Dogs", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant3 = Restaurant(name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Pho", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$8.99", categorie="Hot Dogs", restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chinese Dumplings", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$6.99", categorie="Appetizer", restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Gyoza", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$9.95", categorie="Hot Dogs", restaurant=restaurant3)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Stinky Tofu", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$6.99", categorie="Hot Dogs", restaurant=restaurant3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Veggie Burger", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$9.50", categorie="Burgers", restaurant=restaurant3)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Mineral Water", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$5.99", categorie="Drinks", restaurant=restaurant3)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Cofee Espresso", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$7.99", categorie="Drinks", restaurant=restaurant3)

session.add(menuItem7)
session.commit()


# Menu for The Spiced Cloud
restaurant4 = Restaurant(name="The Spiced Cloud")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Tres Leches Cake", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$2.99", categorie="Appetizer", restaurant=restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom risotto", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$5.99", categorie="Burgers", restaurant=restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$4.50", categorie="Appetizer", restaurant=restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$6.95", categorie="Appetizer", restaurant=restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$7.95", categorie="Burgers", restaurant=restaurant4)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Coca-Cola", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$10.25", categorie="Drinks", restaurant=restaurant3)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Cofee Cappuccino", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                     price="$5.99", categorie="Drinks", restaurant=restaurant3)

session.add(menuItem7)
session.commit()


print ("Database Fulled!")
