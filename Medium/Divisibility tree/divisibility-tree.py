
from typing import List


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        
        def util(adj, u, p, res):
            count = 0
            for v in adj[u]:
                if v != p:
                    x = util(adj, v, u, res)
                    if x%2 == 0:
                        res[0] += 1
                    else:
                        count += x
            return count+1
        
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[1]-1].append(e[0]-1)
            adj[e[0]-1].append(e[1]-1)
        
        res = [0]
        util(adj, 0, -1, res)
        return res[0]
        



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

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends