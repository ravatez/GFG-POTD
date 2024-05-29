
class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        # code here
        dp = [False] * (n + 1)
        if x > y:
            x, y = y, x
        for i in range(1, min(x, n + 1)):
            dp[i] = not dp[i - 1]
        for i in range(x, min(y, n + 1)):
            dp[i] = not (dp[i - 1] and dp[i - x])
        for i in range(y, n + 1):
            dp[i] = not (dp[i - 1] and dp[i - x] and dp[i - y])
        return 1 if dp[n] else 0    



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        obj = Solution()
        res = obj.findWinner(n, x, y)

        print(res)

# } Driver Code Ends