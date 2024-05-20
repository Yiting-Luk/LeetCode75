class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
    def insertAtEnd(self, new_data):
            new_node = Node(new_data)  # Create a new node
            if self.head is None:
                self.head = new_node  # If the list is empty, make the new node the head
                return
            last = self.head 
            while last.next:  # Otherwise, traverse the list to find the last node
                last = last.next
            last.next = new_node  # Make the new node the next node of the last node        
    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data, end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line

llist = LinkedList()

# Insert a word at the end
llist.insertAtEnd('fox')
llist.insertAtEnd('jumps')

# Print the list before deletion
print("List before deletion:")
llist.printList()