#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        dic={}
        reachable=[-1]*n
        for s,t in edges:
            if s not in dic:
                dic[s]=set()
            if t not in dic:
                dic[t]=set()
            dic[s].add(t)
            dic[t].add(s)
        reachable[src]=0
        visited=set()
        visited.add(src)
        if src not in dic:
            return reachable
        q=dic[src]
        step=1
        while q:
            next=[]
            for node in q:
                if node in visited:
                    continue
                visited.add(node)
                reachable[node]=step
                if node in dic:
                    next+=dic[node]
            q=next
            step+=1
        return reachable

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends