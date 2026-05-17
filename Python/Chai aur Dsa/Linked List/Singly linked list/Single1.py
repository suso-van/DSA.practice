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
        
    def display(self): # method to display the elements of the linked list
        current_node = self.head # start from the head and traverse through the linked list
        while current_node:
            print(current_node.data, end=' ') # print the data of each node followed by a space
            current_node = current_node.next # move to the next node
        print() # print a newline after displaying all nodes
        
    def insert_at_beginning(self, data): # method to insert a new node at the beginning of the linked list
        new_node = Node(data) # create a new node with the given data
        new_node.next = self.head # set the next pointer of the new node to the current head
        self.head = new_node # set the new node as the new head of the linked list
        
# Example usage:
linked_list = SinglyLinkedList() # create a new singly linked list
linked_list.insert_at_beginning(5) # insert 5 at the beginning of the linked list
linked_list.insert_at_end(10) # insert 10 at the end of the linked list
linked_list.insert_at_end(20) # insert 20 at the end of the linked list
linked_list.insert_at_end(30) # insert 30 at the end of the linked list
linked_list.display() # display the elements of the linked list 