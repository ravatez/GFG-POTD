class Solution:
    def findUnique(self, arr):
        # code here 
        from functools import reduce
        from operator import xor
        return reduce(xor, arr)

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findUnique(arr)
        print(ans)
        print("~")
# } Driver Code Ends