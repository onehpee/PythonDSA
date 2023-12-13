# Recursion is the process of defining a problem (or the solution to a problem) in terms of (a simpler version of) itself. 
# For example, we can define the operation "find your way home" as: 
#1. If you are at home, stop moving. 
#2. Take one step toward home. 
#3. "find your way home"
# Here the solution to finding your way home is two steps (three steps).
# First, we don't go home if we are already home. 
# Secondly, we do a very simple action that makes our situation simpler to solve. 
# Finally, we redo the entire algorithm.
# The above example is called tail recursion. This is where the very last statement is calling the recursive algorithm. 
# Tail recursion can directly be translated into loops. 
# Another example of recursion would be finding the maximum value in a list of numbers.
# The maximum value in a list is either the first number or the biggest of the remaining numbers.
# Here is how we would write the pseudocode of the algorithm: 


def findMax(self, list):
    self.list = []
    
    possible_max1 = "First value in list"
    possible_max2 = "find max (rest of the list)"
    
    if(possible_max1 > possible_max2):
        print(possible_max1)
    else:
        print(possible_max2)
        
        
#Parts of a Recursive Algorithm
#All recursive algorithms have the following
# 1. Base Case(i.e., when to stop)
# 2. Work toward base case
# 3. Recursive Call(i.e., call ourselves)

# The "work toward base case" is where we make the problem simpler (e.g., divide list into two parts, each smaller than the original).
# The recursive call, is where we use the same algorithm to solve a simpler version of the problem. 
# The base case is the solution to the "simplest" possible problem
# (For example, the base case in the problem 'find the largest number in a list' would be if the list had only one number... 
# and by definition if there is only one number, it is the largest). 

#Example
#Adding three numbers is equivalent to adding the first two numbers, and then adding these two numbers again. 

def add_numbers(*args):
    if (len(args) == 2):
        return sum(args)
    elif(len(args) == 3):
        return sum(args)
    else:
        return
    
# Base Case: if (len(args) == 2) result = a + b;
# "Work toward base case": a+b becomes the first parameter
# This reduces the number of parameters (nargin) sent in to the function from 3 to 2, and 2 is the base case!
# Recursive Call: add_numbers(a+b, c);

# Why Recursion Works
# In a recursive algorithm, the computer "remembers" every previous state of the problem.
# This information is "held" by the computer on the "activation stack" (i.e., inside of each functions workspace).

# Every function has its own workspace PER CALL of the function. 


    
#Maze Example
# Consider a rectangle grid of rooms, where each room may or may not have doors on the North, South, East, and West sides.
# How do you find your way out of a maze? Here is one possible "algorithm" for finding the answer:
# For every door in the current room, if the door leads to the exit, take that door. 
# The "trick" here is of course, how do we know if the door leads to a room that leads to the exit? 
# The answer is we don't but we can let the computer figure it out for us.
# What is the recursive part about the above algorithm? Its the "door leads out of the maze".
# How do we know if a door leads out of the maze? We know because inside the next room (going through the door),
# we ask the same question, how do we get out of the maze?
# What happens is the computer "remembers" all the "what ifs". What if I take the first door, 
# what if I take the second door, what if I take the next door, etc. And for every possible door you can move through, 
# the computer remembers those what ifs, and for every door after that, and after that, etc, until the end is found.   

    
    
    
if __name__ == "__main__":
    print(add_numbers(2,3))