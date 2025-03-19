class Solution:
    def maxProfit(self, prices, k):
        # code here
        # code here
        n = len(arr)
        if k == 0 or n < 2:
            return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if arr[i] > arr[i - 1]:
                    profit += arr[i] - arr[i - 1]
            return profit
        else:
            prev_dp = [0] * n
            for t in range(1, k + 1):
                curr_dp = [0] * n
                max_diff = -arr[0]
                for i in range(1, n):
                    curr_dp[i] = max(curr_dp[i - 1], arr[i] + max_diff)
                    max_diff = max(max_diff, prev_dp[i] - arr[i])
                prev_dp = curr_dp.copy()
            return prev_dp[-1]

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends