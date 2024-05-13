
from typing import List
from collections import deque

class Solution:
    def bfs(self, adj: List[List[int]], start: int, vis: List[int]) -> bool:
        num, edges = 0, 0
        q = deque()
        q.append(start)
        vis[start] = 1
        
        while q:
            node = q.popleft()
            num += 1
            edges += len(adj[node])
            
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    q.append(neighbor)
                    vis[neighbor] = 1
        return num * (num - 1) == edges
        
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # code here
        adj = [[] for _ in range(v+1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        vis = [0] * (v+1)
        ans = 0
        for i in range(1, v+1):
            if self.bfs(adj, i, vis):
                ans += 1
        
        return ans



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        e = int(input())

        v = int(input())

        edges = IntMatrix().Input(e, 2)

        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)

        print(res)

# } Driver Code Ends