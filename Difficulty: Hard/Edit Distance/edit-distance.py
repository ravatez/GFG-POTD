class Solution:
	def editDistance(self, str1, str2):
		# Code here
        m = len(str1)
        n = len(str2)
        
        # Create a table to store results of subproblems
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill dp[][] in bottom up manner
        for i in range(m + 1):
            for j in range(n + 1):
                
                # If first string is empty, only option is to insert all characters of second string
                if i == 0:
                    dp[i][j] = j    # Min. operations = j
                
                # If second string is empty, only option is to remove all characters of first string
                elif j == 0:
                    dp[i][j] = i    # Min. operations = i
                
                # If last characters are same, ignore last character and recur for remaining string
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                # If last character are different, consider all possibilities and find minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],    # Insert
                                       dp[i-1][j],    # Remove
                                       dp[i-1][j-1])  # Replace
        
        return dp[m][n]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends