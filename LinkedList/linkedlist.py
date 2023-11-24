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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        iterate = self.head
        while iterate.next:
            iterate = iterate.next
        iterate.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        iterate = self.head
        while iterate:
            count+=1
            iterate = iterate.next
            
        return count
    
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
    #LL.insert_at_begining(122)
    #LL.insert_at_begining(24)
    #LL.insert_at_end(36)
    LL.insert_values(["Hat", "Bat", "Cat"])
    LL.print()
    LL.insert_at(0,"Flat")
    LL.print()
    LL.insert_at(2,"Mat")
    LL.print()
    
