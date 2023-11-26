#Write a method find of the Node class that is passed a data item as parameter,
#and returns a reference to the first node in the linked list containing that item, 
#or `None’ if the item is not found.

class Node:
    def __init__(self, data):
        self.data = data  # instance variable to store the data
        self.next = None  # instance variable with address of next node

    #  Write your find method here:


# The head is the first node in a linked list.
head = Node("Maine")
another_node = Node("Idaho")
head.next = another_node
a_third_node = Node("Utah")
another_node.next = a_third_node

print("Found:  " + str(head.find("Utah").data))