from math import pi
from math import sqrt
 
#Object-Oriented Programming (OOP) is a programming paradigm in which we can think about complex problems as objects.
# A paradigm is a theory that supplies the base for solving problems.
# So when we’re talking about OOP, we’re referring to a set of concepts and patterns we use to solve problems with objects.
# An object in Pythonn is a single collection of data (attributes) and behavior (methods). You can think of objects as real things around you.

# OOP Allows You to Code Faster
# Coding faster doesn’t mean writing fewer lines of code. It means you can implement more features in less time without compromising the stability of a project.
# Object-Oriented programming allows you to reuse code by implementing abstraction. This principle makes your code more concise and legible.
# As you may know, programmers spend much more time reading code than writing it.
# It’s the reason legibility is always more important than getting features out as quickly as possible.

# Everything Is an Object in Python
# We’ll tell you a secret: you’ve been using OOP all the time without noticing it.
# Even when using other paradigms in Python, you still use objects to do almost everything.
# That’s because, in Python, everything is an object.
# Remember the definition of object: An object in Python is a single collection of data (attributes) and behavior (methods).
# That matches any data type in Python.
# A string is a collection of data (characters) and behaviors (upper(), lower(), etc..). The same applies to integers, floats, booleans, lists, and dictionaries.
# Before continuing, let’s review the meaning of attributes and methods.

# Your First Object in Python
# A class is like a template. It allows you to create custom objects based on the attributes and methods you define.
# You can think of it as a cookie-cutter that you modify to bake the perfect cookies (objects, not tracking cookies), with defined characteristics: Shape, Size, and more.
# On the other hand, we have instances. An instance is an individual object of a class, which has a unique memory address.

class Cookies:
    pass

cookie1 = Cookies()

# Constructor Method
# The __init__() method is also named “constructor.” It’s called Python each time we instantiate an object.
# The constructor creates the object’s initial state with the minimum set of parameters it needs to exist. Let’s modify the Cookie class, so it accepts parameters in its constructor.

class Cookie:
	# Constructor
	def __init__(self, name, shape, chips='Chocolate'):
		# Instance attributes
		self.name = name
		self.shape = shape
		self.chips = chips

	# The object is passing itself as a parameter
	def bake(self):
		print(f'This {self.name}, is being baked with the shape {self.shape} and chips of {self.chips}')
		print('Enjoy your cookie!')
  
  
# 1. Abstraction

# Abstraction hides the internal functionality of an application from the user. The user could be either the end client or other developers.
# We can find abstraction in our daily lives. For example, you know how to use your phone, but you probably don’t know exactly what’s happening inside it each time you open an app.
# Another example is Python itself. You know how to use it to build functional software, and you can do it even if you don’t understand Python’s inner workings.
# Applying the same to code allows you to collect all the objects in a problem and abstract standard functionality into classes.


# 2. Inheritance
# Inheritance allows us to define multiple subclasses from an already defined class.
# The primary purpose of it is to follow the DRY principle. You’ll be able to reuse a lot of code by implementing all the sharing components into superclasses.
# You can think of it as the real-life concept of genetic inheritance. Children (subclass) are the result of inheritance between two parents (superclasses). 
# They inherit all the physical characteristics (attributes) and some common behaviors (methods).



# 3. Polymorphism
# Polymorphism lets us slightly modify methods and attributes of the subclasses previously defined in the superclass.
# The literal meaning is “many forms.” That’s because we build methods with the same name but different functionality.
# Going back to the previous idea, children are also a perfect example of polymorphism. They can inherit a defined behavior get_hungry() but in a slightly different way,
# for instance, getting hungry every 4 hours instead of every 6.



# 4. Encapsulation
# Encapsulation is the process in which we protect the internal integrity of data in a class.
# Although there isn’t a private statement in Python, you can apply encapsulation by using mangling in Python.
# There are special methods named getters and setters that allow us to access unique attributes and methods.
# Let’s imagine a Human class that has a unique attribute named _height. You can modify this attribute only within certain constraints 
# (it’s nearly impossible to be higher than 3 meters).



class Shape:
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def get_area(self):
		return self.side1 * self.side2

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'


class Rectangle(Shape): # Superclass in Parenthesis
	pass

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)
  
class Triangle(Rectangle):
	def __init__(self, base, height):
		super().__init__(base, height)
 
	def get_area(self):
		area = super().get_area()
		return area / 2


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
 
	def get_area(self):
		return pi * (self.radius ** 2)

class Hexagon(Rectangle):
	
	def get_area(self):
		return (3 * sqrt(3) * self.side1 ** 2) / 2

breakpoint()