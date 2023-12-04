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