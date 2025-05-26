
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
     
        
class Solution:
    def sortedInsert(self, head, data):
        prv=head
        cur=head.next
        while 1:
            ok=prv.data<=data and data<=cur.data
            ok=ok or prv.data<=data and cur==head
            ok=ok or data<=cur.data and cur==head
            if ok:
                break
            prv=cur
            cur=cur.next
        prv.next=Node(data)
        prv.next.next=cur
        return head if head.data<=data else prv.next