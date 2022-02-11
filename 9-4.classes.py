# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print
# it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number
# and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
      def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type
            self.number_served = 3

      def describe_restaurant(self):
            print(self.name + " is an " + self.cuisine_type + " restaurant")

      def open_restaurant(self):
            print(f"The {self.name} is open")

      def set_number_served(self, number):
          self.number_served = number
          print(f"The restaurant has served {number} people until today")
      
      def increment_number_served(self, new_number):
          self.number_served += new_number
          print(f"The restaurant has served {self.number_served} people in total") 
      
restaurant = Restaurant("Trattoria", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(100)
restaurant.increment_number_served(20)