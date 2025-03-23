#User function Template for python3
class Solution:
	def countWays(self, digits):
		# Code here
		# Code here
        n = len(digits)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(n):
            if digits[i] != '0':
                dp[i+1] += dp[i]
            if i-1 >= 0 and digits[i-1] != '0' and int(digits[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends