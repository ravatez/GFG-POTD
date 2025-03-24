class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

    

        for l in range(2, n):

            # tu copy kr le re baba

            for i in range(1, n - l + 1):

                j = i + l - 1

                dp[i][j] = float('inf')

                for k in range(i, j):

                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j])

                # tu copy kr le re baba

        return dp[1][n-1]       
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends