#User function Template for python3

#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
            
        def isValid(i, j):
            for row in range(n):
                if grid[i][row] == 'Q':
                    return False
            for col in range(n):
                if grid[col][j] == 'Q':
                    return False
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                if grid[x][y] == 'Q':
                    return False
                x, y = x - 1, y - 1
            x, y = i + 1, j + 1
            while x < n and y < n:
                if grid[x][y] == 'Q':
                    return False
                x, y = x + 1, y + 1
            x, y = i - 1, j + 1
            while x >= 0 and y < n:
                if grid[x][y] == 'Q':
                    return False
                x, y = x - 1, y + 1
            x, y = i + 1, j - 1
            while x < n and y >= 0:
                if grid[x][y] == 'Q':
                    return False
                x, y = x + 1, y - 1
            
            return True
        
        def f(col):
            if col >= n:
                l = []
                for column in range(n):
                    for i in range(n):
                        if grid[i][column] == 'Q':
                            l.append(i + 1)
                            break
                res.append(l)
                return
            
            for row in range(n):
                if grid[row][col] == 0 and isValid(row, col):
                    grid[row][col] = 'Q'
                    f(col + 1)
                    grid[row][col] = 0
                    
        grid = [[0] * n for _ in range(n)]
        res = []
        f(0)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends