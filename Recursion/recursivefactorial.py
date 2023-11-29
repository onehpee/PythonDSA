#Write the function factorial with no loops, 
#based on the observation above. You need to handle two cases. 
#First, if the parameter n has the value 0, 
#then factorial(n) should simply return 1. 
#Compute n! recursively.
def factorial(n):
    # you write this part
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))