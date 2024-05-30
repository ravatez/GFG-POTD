
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        MOD = 10**9 + 7
        n = len(s1)
        m = len(s2)
        
        # Create DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize dp[i][0] to 1
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
                else:
                    dp[i][j] = dp[i-1][j] % MOD
        
        return dp[n][m]    



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends