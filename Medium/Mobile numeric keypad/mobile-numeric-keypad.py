#User function Template for python3
class Solution:
	def getCount(self, n):
		# code here
        numbers = [[0, 8], [1, 2, 4], [2, 1, 3, 5], [3, 2, 6], [4, 1, 5, 7], [5, 2, 4, 6, 8], [6, 3, 5, 9], [7, 4, 8], [8, 5, 7, 9, 0], [9, 6, 8]]

        def solve(num, count, dp):
            if count == 0:
                return 1

            if dp[num][count] != -1:
                return dp[num][count]

            total = 0
            for i in numbers[num]:
                total += solve(i, count - 1, dp)

            dp[num][count] = total
            return dp[num][count]

        dp = [[-1] * n for _ in range(10)]
        total = 0
        for i in range(10):
            total += solve(i, n - 1, dp)

        return total

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends