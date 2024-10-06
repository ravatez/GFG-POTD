#User function Template for python3
class Solution:
    def numIslands(self, grid):
        # code here
        def f(i,j,vis):
            for r,c in [[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,-1],[1,1],[-1,-1]]:
                nr,nc = i+r,c+j
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in vis and grid[nr][nc] != 0:
                    vis.add((nr,nc))
                    f(nr,nc,vis)
        cnt, vis = 0,set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i,j) not in vis:
                    cnt += 1
                    vis.add((i,j))
                    f(i,j,vis)
        return cnt
        
#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends