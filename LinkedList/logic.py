#A linked list is a data structure made up of many nodes 
#Nodes can contain data
#The nodes can be linked
#The first node is the head/position 0
#The last node is the tail
#It is a ordered data structure

#linked list has positions and nodes
#linked list insertion will be constant 0 of 1 time
#Doesn't have to be contiguousl, can exist anywhere in memory addressing
#You don't have to shift elements, just change the nodes next pointer
#Array has index and elements stored contiguously or right next to eachother
#When you insert and element you have to shift every element n amount of times

#Transversing through a linked list

#head = "the beginning of the linked list"
#Null/None = "the end of the linked list"
#current = the current node you are on 
#current.next = is the next node
#current = current.next = is setting your current position to the next node
#current = Null = means reaching the end of the linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        iterater = self.head
        linklist_string = " "

        while iterater:
            linklist_string += str(iterater.data) + "-->"
            iterater = iterater.next
        print(linklist_string)
        
    # def linkedlistvalues(self,head):
    #     values = []
    #     current = head
    #     while current != None:
    #         values.insert(current.data)        
    #         current = current.next
    #         return values
        
        
if __name__ == "__main__":
    LL = LinkedList()
    LL.linkedlistvalues("A")
    LL.linkedlistvalues("B")
    LL.linkedlistvalues("C")
    LL.linkedlistvalues("D")
    LL.print()
    