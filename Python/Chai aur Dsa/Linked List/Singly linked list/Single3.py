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
        
    def delete_node(self, key): # method to delete a node with a specific key from the linked list
        current_node = self.head # start from the head and traverse through the linked list
        previous_node = None
        while current_node and current_node.data != key: # find the node with the given key
            previous_node = current_node
            current_node = current_node.next
        if current_node is None: # if the key is not found in the linked list, do nothing
            print("Key not found in the linked list")
            return
        if previous_node is None: # if the node to be deleted is the head, update the head to the next node
            self.head = current_node.next
        else: # otherwise, update the next pointer of the previous node to skip the current node
            previous_node.next = current_node.next
            current_node.next = None # optional: explicitly set the next pointer of the deleted node to None    
        
    def display(self): # method to display the elements of the linked list
        current_node = self.head # start from the head and traverse through the linked list
        while current_node:
            print(current_node.data, end=' ') # print the data of each node followed by a space
            current_node = current_node.next # move to the next node
        print() # print a newline after displaying all nodes
        
# Example usage:
linked_list = SinglyLinkedList() # create a new singly linked list
linked_list.insert_at_end(10) # insert 10 at the end of the linked list
linked_list.insert_at_end(20) # insert 20 at the end of the linked list
linked_list.insert_at_end(30)# insert 30 at the end of the linked list
linked_list.delete_node(20) # delete the node with data 20 from the linked list
linked_list.display() # display the elements of the linked list 