
class Solution:
    def countWays(self, n):
        # code here
        # code here
        def f(n):
            if n<0:
                return 0
            if n==0:
                return 1
            if n in dp:
                return dp[n]
            dp[n]=f(n-1)+f(n-2)
            return dp[n]
        dp={}
        return f(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends