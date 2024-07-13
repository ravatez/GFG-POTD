#User function Template for python3
import heapq
from collections import defaultdict
import sys
from typing import List

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        if n == 1:
            return [0, 1]  # Single node graph, path from node 1 to itself

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Dijkstra's Algorithm
        distances = {i: sys.maxsize for i in range(1, n + 1)}
        distances[1] = 0
        priority_queue = [(0, 1)]  # (distance, node)
        parent = {1: None}
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        if distances[n] == sys.maxsize:
            return [-1]
        
        # Reconstruct path from 1 to n
        path = []
        current = n
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        
        return [distances[n]] + path    


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends