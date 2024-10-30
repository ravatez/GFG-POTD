#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
        node=Node(x)
        dummy=Node(-float('inf'))
        dummy.next=head
        head.prev=dummy
        cur=dummy
        while cur:
            if cur.next and cur.next.data>=x:
                node.next=cur.next
                cur.next=node
                node.next.prev=node
                node.prev=cur
                break
            prv=cur
            cur=cur.next
        if not cur:
            prv.next=node
            node.prev=prv
        nhead=dummy.next
        nhead.prev=None
        return nhead

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        values = list(map(int, input().strip().split()))
        head = None
        tail = None

        for value in values:
            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        value_to_insert = int(input().strip())
        solution = Solution()
        head = solution.sortedInsert(head, value_to_insert)
        print_list(head)

        print("~")

# } Driver Code Ends