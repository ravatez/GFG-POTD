class Solution:  
    def findMaxSum(self,arr):
        # code here
        prev_max = [0, 0]  # [if looted house, not looted house]
        for val in arr:
            if_looted = prev_max[1] + val
            not_looted = max(prev_max)
            prev_max = [if_looted, not_looted]
        return max(prev_max)

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends