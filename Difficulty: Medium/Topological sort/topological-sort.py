class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        # Convert edges to adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        def dfs(node, visited, stack):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour, visited, stack)
            stack.append(node)

        visited = [False] * V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)

        return stack[::-1]


#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        x = V
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, x, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends