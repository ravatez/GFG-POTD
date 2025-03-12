#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n=len(cost)
        a,b=cost[0],cost[1]
        for i in range(2,n):
            c=cost[i]+min(b,a)
            a,b=b,c
        return min(a,b)        


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends