#A program that adds all of the even numbers from 0 to 100 to a linked list, and then prints out all of the items in the list.
class Node:
    def __init__(self, data):
        self.data = data  # instance variable to store the data
        self.next = None  # instance variable with address of next node

# Nodes:
head = Node(0)
current = head
for i in range(1, 51):
    current.next = Node(2 * i)
    current = current.next

# Print the data of the list in order:
current = head   # copy the address of the head node into node
while current != None:
    print(current.data)
    current = current.next