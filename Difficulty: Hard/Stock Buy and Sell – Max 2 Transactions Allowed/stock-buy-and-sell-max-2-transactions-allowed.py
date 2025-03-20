class Solution:
    def maxProfit(self, prices):
        # code here
        # code here
        n=len(prices)
        #create 2d array with n*k size k number of row and each row n elements assigned to zero
        dp=[[0] * n for _ in range(3)]
        if n<=1:
            return 0
        for i in range(1,3):
            dif=-prices[0] 
            for j in range(1,n):
                #at first dp[1][0],prices[1]+dif(-10) then you will get
                dp[i][j]=max(dp[i][j-1],prices[j]+dif)
                #dif find dif and dp[i-1][j]-prices[j]
                dif=max(dif,dp[i-1][j]-prices[j])
        return dp[2][n-1]

#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends