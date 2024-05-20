# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
    def insertAtEnd(self, new_data):
            new_node = ListNode(new_data)  # Create a new node
            if self.head is None:
                self.head = new_node  # If the list is empty, make the new node the head
                return
            last = self.head 
            while last.next:  # Otherwise, traverse the list to find the last node
                last = last.next
            last.next = new_node  # Make the new node the next node of the last node        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                
            return prev

head = [1,2,3,4,5]
llsit = LinkedList()
for val in head:
    llsit.insertAtEnd(val)
obj = Solution()
result = obj.reverseList(llsit.head)
print(result.val)