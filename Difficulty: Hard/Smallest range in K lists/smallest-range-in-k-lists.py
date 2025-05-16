class Solution:
    def findSmallestRange(self, arr):
        # code here
        from heapq import heapify, heapreplace
        k, n = len(arr), len(arr[0])
        h = [(arr[i][0], i, 0) for i in range(k)]
        heapify(h)
        max_in_h, _, _ = max(h)
        lo, hi = 0, 10**5
        while True:
            min_in_h, i, j = h[0]
            if hi - lo > max_in_h - min_in_h:
                lo, hi = min_in_h, max_in_h
            if j == n - 1:
                break
            if arr[i][j + 1] > max_in_h:
                max_in_h = arr[i][j + 1]
            heapreplace(h, (arr[i][j + 1], i, j + 1))
        return [lo, hi]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends