
from typing import List


class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # code here
        dp = [0] * n
        
        ans = 0
        # Iterate from the end of the array to the beginning
        for i in range(n-1, -1, -1):
            maxi = 0
            # Check subsequent elements
            for j in range(i+1, n):
                if abs(a[i] - a[j]) == 1:
                    maxi = max(maxi, dp[j])
            dp[i] = 1 + maxi
            ans = max(ans, dp[i])
        
        return ans



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.longestSubseq(n, a)

        print(res)

# } Driver Code Ends