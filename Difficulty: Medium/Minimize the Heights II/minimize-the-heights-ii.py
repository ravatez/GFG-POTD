#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        arr.sort()
        a, s, l = arr[-1] - arr[0], arr[0] + k, arr[-1] - k
        for i in range(n - 1):
            m = min(s, arr[i + 1] - k)
            M = max(l, arr[i] + k )
            if m >= 0:
                a = min(a, M - m)
        return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends