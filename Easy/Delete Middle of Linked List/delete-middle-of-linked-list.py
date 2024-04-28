#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteMid(self, head):
        # If the list is empty or has only one node
        if not head or not head.next:
            return None

        # Initialize slow, fast, and prev pointers
        slow = fast = head
        prev = None

        # Move fast pointer two steps at a time
        # and slow pointer one step at a time
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # If the number of nodes is odd
        if fast:
            prev.next = slow.next
        # If the number of nodes is even
        else:
            prev.next = prev.next.next

        return head

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        obj = Solution();
        res=obj.deleteMid(ll.head)
        printList(res)
# } Driver Code Ends