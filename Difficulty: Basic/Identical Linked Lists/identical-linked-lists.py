# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    # Initialization :Two empty lists, l1 and l2, are initialized to store the data from the nodes of the two linked lists.
    l1=[]
    l2=[]
    # Transverse  both linked list : This while loop iterates through the first linked list (head1). For each node, it appends the node's data to the list l1 and then moves to the next node.
    while head1:
        l1.append(head1.data)
        head1=head1.next
    while head2:
        l2.append(head2.data)
        head2=head2.next
    # Comparing  both lists :After traversing both linked lists and storing their data in l1 and l2, this if statement checks if l1 is equal to l2. If they are identical (i.e.,contain the same elements in the same order), the function returns 1. Otherwise, it returns 0.
    if l1==l2:
        return 1
    else:
        return 0

#{ 
 # Driver Code Starts
# Node Class
class node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if (areIdentical(head1, head2)):
            print('true')
        else:
            print('false')

# } Driver Code Ends