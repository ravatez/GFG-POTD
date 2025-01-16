class Solution:
    def maxLen(self, arr):
        # code here
        n=len(arr)
        for i in range(n):
            if arr[i]==0:
                arr[i]=-1

        # print(arr) 
        d={0:-1}
        maxi=0
        curr=0
        for i in range(n):
            curr+=arr[i]
            if curr in d:
                # print(i,d[curr])
                maxi=max(maxi,i-d[curr])
            else:
                d[curr]=i
        
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends