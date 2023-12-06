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

class Node:
    def __init__(self, data=None, next=None):
        self.data = data    
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
            
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iterate = self.head
        while iterate:
            if count == index - 1:
                iterate.next = iterate.next.next
                break
            
            iterate = iterate.next
            count += 1
    
    def insert_at(self, index, data):
        if index <0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        iterate = self.head
        while iterate:
            if count == index - 1:
                node = Node(data, iterate.next)
                iterate.next = node
                break
            
        iterate = iterate.next
        count += 1       
            

if __name__ == "__main__":
    LL = LinkedList()
    LL.insert_at_begining(122)
    LL.insert_at_begining(24)
    LL.insert_at_end(36)