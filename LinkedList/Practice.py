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
            
            

if __name__ == "__main__":
    LL = LinkedList()
    LL.insert_at_begining(122)
    LL.insert_at_begining(24)
    LL.insert_at_end(36)