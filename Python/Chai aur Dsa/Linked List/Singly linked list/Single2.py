class Node:
    def __init__(self, data, next=None): # constructor to initialize the node with data and next pointer 
        self.data = data
        self.next = next
        
class SinglyLinkedList:
    def __init__(self): # constructor to initialize the head of the linked list
        self.head = None
        
    def insert_at_end(self, data): # method to insert a new node at the end of the linked list
        new_node = Node(data) # create a new node with the given data
        if self.head is None: # if the linked list is empty, set the new node as the head
            self.head = new_node
            return
        last_node = self.head # start from the head and traverse to the end of the linked list
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node # set the next pointer of the last node to the new node
        
    def insert_at_middle(self, data, position): # use for searching algorithm
                                                # method to insert a new node at a specific position in the linked list
        new_node = Node(data) # create a new node with the given data
        if position == 0: # if the position is 0, insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head # start from the head and traverse to the desired position
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if current_node is None: # if the position is out of bounds, do not insert
            print("Position out of bounds")
            return
        new_node.next = current_node.next # set the next pointer of the new node to the next node of the current node
        current_node.next = new_node # set the next pointer of the current node to the new node
        
    def display(self): # method to display the elements of the linked list
        current_node = self.head # start from the head and traverse through the linked list
        while current_node:
            print(current_node.data, end=' ') # print the data of each node followed by a space
            current_node = current_node.next # move to the next node
        print() # print a newline after displaying all nodes
        
    
        
# Example usage:
linked_list = SinglyLinkedList() # create a new singly linked list
linked_list.insert_at_end(10) # insert 10 at the end of the linked list
linked_list.insert_at_end(20)# insert 20 at the end of the linked list
linked_list.insert_at_end(30) # insert 30 at the end of the linked list
linked_list.insert_at_middle(15, 2) # insert 15 at position 2 in the linked list
linked_list.display() # display the elements of the linked list 