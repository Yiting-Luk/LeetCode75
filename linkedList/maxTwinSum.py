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
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        data = []
        while head != None:
            data.append(head.val)
            head = head.next
        left = 0
        right = len(data)-1
        pairSum = []
        while left < right:
            pairSum.append(data[left]+data[right])
            left += 1
            right -= 1
        return max(pairSum)

head = [5,4,2,1]
llist = LinkedList()
for val in head:
    llist.insertAtEnd(val)

obj = Solution()
result = obj.pairSum(llist.head)
print(result)
