class Node:
    def __init__(self, data):# constructor to initialize the node with data, next pointer and previous pointer
        self.data = data 
        self.next = None # initialize the next pointer to None
        self.prev = None # initialize the previous pointer to None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # Adding a new node at the end of the list
        new_node = Node(data) # create a new node with the given data
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        
    def insert_at_beginning(self, data): # method to insert a new node at the beginning of the linked list
        new_node = Node(data) # create a new node with the given data
        if not self.head: # if the linked list is empty, set the new node as the head
            self.head = new_node
            return
        new_node.next = self.head # set the next pointer of the new node to the current head
        self.head.prev = new_node # set the previous pointer of the current head to the new node
        self.head = new_node # set the new node as the new head of the linked list
    
    def delete_node(self, key): # method to delete a node with a specific key from the linked list
        current_node = self.head
        while current_node:
            if current_node.data == key: # if the node to be deleted is found
                if current_node.prev: # if there is a previous node, set its next pointer to the next node of the current node
                    current_node.prev.next = current_node.next
                else: # if there is no previous node, set the next node as the new head
                    self.head = current_node.next
                if current_node.next: # if there is a next node, set its previous pointer to the previous node of the current node
                    current_node.next.prev = current_node.prev
                return # exit the method after deleting the node
            current_node = current_node.next # move to the next node

    def display(self): # method to display the elements of the linked list
        current_node = self.head # start from the head and traverse through the linked list
        while current_node: # print the data of each node followed by a space
            print(current_node.data, end=" <<-->> ")
            current_node = current_node.next
        print()
        
# Example usage:
double_linked_list = DoubleLinkedList() # create a new double linked list
double_linked_list.append(10) # append 10 to the end of the double linked list
double_linked_list.append(20) # append 20 to the end of the double linked list
double_linked_list.append(30) # append 30 to the end of the double linked list
double_linked_list.insert_at_beginning(5) # insert 5 at the beginning of the double linked list
double_linked_list.delete_node(20) # delete the node with data 20 from the double linked list
double_linked_list.display() # display the elements of the double linked list       
