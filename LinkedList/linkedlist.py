class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
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
        
        
        
if __name__ == "__main__":
    LL = LinkedList()
    LL.insert_at_begining(12)
    LL.insert_at_begining(24)
    LL.print()