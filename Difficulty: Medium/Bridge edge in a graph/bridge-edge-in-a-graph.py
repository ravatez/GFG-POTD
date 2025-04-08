class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        adj = [[] for _ in range(V)]
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c): # this remove the edges between c to d
                continue
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False]*V
        
        def dfs(start):
            visit[start]=True
            for neigh in adj[start]:
                if not visit[neigh]:
                    dfs(neigh)
        dfs(c) # dfs start from c
        return not visit[d]  # checking d is visited or not


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends