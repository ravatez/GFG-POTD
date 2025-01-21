"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        # Code here
        g_s = None
        g_n = head
        g_p = None
        
        while g_n:
            
            k_s = g_n
            k_e = g_n
            
            cnt=0
            
            while cnt<k and g_n:
                cnt+=1
                k_e = g_n
                g_n = g_n.next
            
            curr=k_s
            prev=None
            
            # print(k_s.data,k_e.data)
            # print("---")
            
            while curr and curr!=g_n:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
            
            if not g_s:
                g_s = prev
            
            if g_p:
                g_p.next = prev
                
            g_p = k_s
            
        return g_s

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends