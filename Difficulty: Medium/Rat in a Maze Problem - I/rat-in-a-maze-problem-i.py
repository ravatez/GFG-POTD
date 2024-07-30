from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        ans=[]
        v=[[0]*n for _ in range (n)]
        
        # 1 up 2 right 3 down 4 left
        def traverse(i, j, direct, predirect):
            if i == j == n - 1:
                ans.append(direct)
                return
            v[i][j]=1
            if i > 0 and predirect != 3 and m[i - 1][j] == 1 and v[i - 1][j] == 0:
                
                traverse(i - 1, j, direct + "U", 1)
            if i < n - 1 and predirect != 1 and m[i + 1][j] == 1 and v[i + 1][j] == 0:
                
                traverse(i + 1, j, direct + "D", 3)
            if j > 0 and predirect != 2 and m[i][j - 1] == 1 and v[i][j - 1] == 0 :
                
                traverse(i, j - 1, direct + "L", 4)
            if j < n - 1 and predirect != 4 and m[i][j + 1] == 1 and v[i][j + 1] == 0:
                
                traverse(i, j + 1, direct + "R", 2)
            v[i][j] = 0 
            return
        if m[0][0]==1:
            traverse(0,0,"",0)
        return ans


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends