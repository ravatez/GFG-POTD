#User function Template for python3

class Solution:
	def lps(self, str):
		# code here
        n = len(str)
        dp = [0]*(n)
        
        for i in range(1, n):
            j = dp[i-1]
            while j > 0 and str[j] != str[i]:
                j = dp[j-1]
            dp[i] = j + int(str[j] == str[i])
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends