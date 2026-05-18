class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        
    def display(self):
        current_node = self.head
        if not self.head:
            print("List is empty")
            return
        while True:
            print(current_node.data, end='<-->')
            current_node = current_node.next
            if current_node == self.head:
                break
        print()
        
# Example usage:
circular_linked_list = CircularLinkedList()
circular_linked_list.append(10)
circular_linked_list.append(20)
circular_linked_list.append(30)
circular_linked_list.display()  
