# Definition for singly-linked list.
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
            else:
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
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            odd = Node(0) 
            odd_ptr = odd # pinter travelsal 
            even = Node(0)
            even_ptr = even 
            idx = 1 
            while head != None :
                if idx % 2 == 0:
                    even_ptr.next = head
                    even_ptr = even_ptr.next
                else:
                    odd_ptr.next = head
                    odd_ptr = odd_ptr.next
                head = head.next
                idx+=1
            even_ptr.next = None
            odd_ptr.next = even.next
            return odd.next

head = [1,2,3,4,5]
llist = LinkedList()
for val in head:
    llist.insertAtEnd(val)
# Print the list before deletion
llist.printList()

obj = Solution()
result = obj.oddEvenList(llist.head)
