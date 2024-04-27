#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution():

    # Function to get the middle node of the Doubly Linked List
    def getMiddle(self, head):
        if not head:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Function to merge two sorted Doubly Linked Lists
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        dummy = Node(0)
        tail = dummy

        while left and right:
            if left.data < right.data:
                tail.next = left
                left.prev = tail
                left = left.next
            else:
                tail.next = right
                right.prev = tail
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
            left.prev = tail
        if right:
            tail.next = right
            right.prev = tail

        head = dummy.next
        head.prev = None
        return head

    #Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self, head):
        if not head or not head.next:
            return head

        # Split the Doubly Linked List into two halves
        middle = self.getMiddle(head)
        right = middle.next
        middle.next = None
        right.prev = None

        # Recursively sort the left and right halves
        left = self.sortDoubly(head)
        right = self.sortDoubly(right)

        # Merge the sorted left and right halves
        sorted_head = self.merge(left, right)

        # Return the head of the sorted Doubly Linked List
        return sorted_head
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends