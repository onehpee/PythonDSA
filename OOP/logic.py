#Object-Oriented Programming (OOP) is a programming paradigm in which we can think about complex problems as objects.
# A paradigm is a theory that supplies the base for solving problems.
# So when we’re talking about OOP, we’re referring to a set of concepts and patterns we use to solve problems with objects.
# An object in Python is a single collection of data (attributes) and behavior (methods). You can think of objects as real things around you.

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