#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        import operator
        from functools import reduce
        return reduce(operator.xor, (i ^ a for i, a in enumerate(arr, 1)), n)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends