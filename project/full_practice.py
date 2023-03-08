import math

print("P value")
print(math.pi)

# Variables
fruits = ["orange","cherry","apple","pinapple"]
o, c, a, p = fruits

print(o, a)


name = "Anthonia"
length = 3   # an integer
kilograms = 73.5 # A float
diameter = 13.6363 

# a set
my_class = {"Math", "French", "403", "Friends"}
print(my_class)

# a dictionary
contact_form = {
    "name": "Anthonia",
    "age": 25,
    "occupation": "Data Scientist",
    "date_of_birth": "13-06-02"
}

contact_form["name"] = "Stella"
first_name = contact_form["name"]
print(first_name)

# a tuple
coffee_queue_name = ("bjorn", "joe", "nenad", "anna", "anna")

print("The first to get coffee")
print(coffee_queue_name[0])

print("The last to get coffee")
print(coffee_queue_name[4])



my_destination = "Paris"

if my_destination == "Paris":
  print("Take the street 1")

elif my_destination == "London":
  print("Take the street 2")

elif my_destination == "New York":
  print("Take the street 3")

else:
  print("I do not know where you are going.")

title_you_search_for = "Python Variables"

python_book_page_titles = {
   "1":"Introduction",
   "2":"Why Python",
   "3":"What is Python",
   "4":"Python Variables",
   "5":"Python Conditions",
   "6":"Data types: sets",
   "7":"Data types: dictionaries",
   "8":"Summary",
   "9":"Author's notes",
   "10":"The end"
}

for i in (1,2,3,4,5,6,7,8,9,10):

  if python_book_page_titles[str(i)] == title_you_search_for:
    print("The page number you are looking for is ")
    print(i)

  else:
    print("It is not on this page, looking on the next...")


def do_the_math(a, b): # Define a new function
  sum_a_b = a + b
  return sum_a_b

find_the_sum = do_the_math(1, 4) # Call the function

print(find_the_sum)


class Cat: # Create a new class called "Cat"

  def __init__(self, name, age, weight, fur_color, favorite_food, number_of_meals, favorite_game):
    # attributes
    self.name = name
    self.age = age
    self.weight = weight
    self.fur_color = fur_color
    self.favorite_food = favorite_food
    self.number_of_meals = number_of_meals
    self.favorite_game = favorite_game
    
  # a method called feed_this_cat
  def feed_this_cat(self): 
    print("The cat is eating now...")
    print("The cat is eating still...")
    print("The cat is happy again!")

my_cat = Cat("Rocky", 12, "11kg", "black", "crackers", "3", "running in circles")   
# Creates an object out of the Cat class and stores it into the my_cat variable

print(my_cat.name) # Print "Rocky"
print(my_cat.weight) # Prints "12kg"
my_cat.feed_this_cat()


# https://igorjovanovic.info/python-beginners-guide/?ad=quora-python-quizz