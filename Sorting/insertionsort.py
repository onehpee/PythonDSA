#The code for insertion sort includes an outer loop
#and an inner loop. The inner loop takes an item, 
#the key, at some index in the list, and slides items 
#one to the right until the correct space has been made
#available to place the key. Write a function insert that 
#takes as parameters a list and the index of the key, and 
#inserts the key into the correct location.
#Re-write insertion sort to use insert.

def insertion_sort(the_list):
    n = len(the_list)   # how many items to sort

    for i in range(1, n):
        key = the_list[i]   # remember what was in the ith position

        j = i - 1     # look in positions to the left of i
        while j >= 0 and the_list[j] > key:
            the_list[j + 1] = the_list[j]
            j -= 1

        the_list[j + 1] = key

grade_list = [89, 45, 85, 81, 77, 94, 22, 79, 92, 91]
insertion_sort(grade_list)
print(grade_list)