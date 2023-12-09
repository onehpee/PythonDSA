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