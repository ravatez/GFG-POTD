class Solution:
    def articulationPoints(self, V, edges):
        # code here
        from collections import defaultdict
    
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
    
        disc, low, time = [-1]*V, [-1]*V, 0
        ret = set()
    
        def dfs(u, p=-1):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            children = 0
            for v in g[u]:
                if disc[v] == -1:  # Not visited
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if p != -1 and low[v] >= disc[u]:
                        ret.add(u)
                elif v != p:
                    low[u] = min(low[u], disc[v])
            if p == -1 and children > 1:
                ret.add(u)
    
        for u in range(V):
            if disc[u] == -1:
                dfs(u)
    
        return sorted(ret) if ret else [-1]

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends