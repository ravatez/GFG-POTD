import heapq
from collections import defaultdict
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        l=defaultdict(list)
        for i,j,k in edges:
            l[i].append((j,k))
            l[j].append((i,k))


        r=[float('inf')]*V
        r[src]=0
        s=[(0,src)]


        while s:
            t1,t2=heapq.heappop(s)
            if t1>r[t2]:continue
            for j,k in l[t2]:
                if r[t2]+k<r[j]:
                    r[j]=r[t2]+k
                    heapq.heappush(s,(r[j],j))


        return r
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends