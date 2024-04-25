#User function Template for python3

class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        max_sum = float('-inf')  # Initialize max_sum with negative infinity
        found_hourglass = False  # Flag to check if at least one hourglass is found
    
        for i in range(n - 2):
            for j in range(m - 2):
                hourglass_sum = (
                    mat[i][j]
                    + mat[i][j + 1]
                    + mat[i][j + 2]
                    + mat[i + 1][j + 1]
                    + mat[i + 2][j]
                    + mat[i + 2][j + 1]
                    + mat[i + 2][j + 2]
                )
                max_sum = max(max_sum, hourglass_sum)
                found_hourglass = True  # Set flag to True since at least one hourglass is found
    
        if found_hourglass:
            return max_sum
        else:
            return -1  # Return -1 if no hourglass is found

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends