class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here
        graph = [[]for _ in range(V)]
        for u,v in edges:
            graph[u].append(v)
        dp = [-1]*V
        visited = [False for _ in range(V)]
        count = self.dfs(graph,src,dest,visited,dp)
        return count
        
    def dfs(self,graph,src,dest,visited,dp):
        
        if src==dest:
            return 1
        if dp[src]!=-1:
            return dp[src]
        count = 0
        for nev in graph[src]:
            if not visited[nev]:
                visited[src] = True
                count += self.dfs(graph,nev,dest,visited,dp)
                visited[src] = False
        dp[src] = count 
        return count