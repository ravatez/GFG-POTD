class Solution:
    def missingNum(self, arr):
        # code here
        arr.sort()
        if(max(arr)==arr[-1] and len(arr)==max(arr)):
            return arr[-1]+1
        else:
            n=max(arr)
            return (n*(n+1)//2)-sum(arr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends