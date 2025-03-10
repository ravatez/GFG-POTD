class Solution:
	def editDistance(self, s1, s2):
		# Code here
        # Code here
        n1=len(s1)
        n2=len(s2)
        dp = [[float("inf")]*(len(s2)+1) for _ in range(len(s1)+1)]
        
        for j in range(n2+1):
            dp[n1][j] = n2-j
        
        for i in range(n1+1):
            dp[i][n2] = n1-i
            
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
         
        return dp[0][0]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends